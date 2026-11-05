/**
 * Rede NAPeN — Motor de Visualização de Diagramas SVG (Pan & Zoom)
 * Suporta arrastar (pan), rolagem (zoom), botões de zoom, reset 100% e atalhos de teclado.
 * Compatível com execução local (file://) e servidores web (http/https).
 */

class SVGViewer {
  constructor(options = {}) {
    this.modalEl = document.getElementById(options.modalId || 'svgModal');
    this.stageEl = document.getElementById(options.stageId || 'svgStage');
    this.containerEl = document.getElementById(options.containerId || 'svgContainer');
    this.titleEl = document.getElementById(options.titleId || 'svgModalTitle');
    this.badgeEl = document.getElementById(options.badgeId || 'svgModalBadge');
    this.zoomTextEl = document.getElementById(options.zoomTextId || 'toolbarZoomText');

    this.scale = 1;
    this.translateX = 0;
    this.translateY = 0;
    this.minScale = 0.2;
    this.maxScale = 5.0;

    this.isDragging = false;
    this.startX = 0;
    this.startY = 0;

    this.currentRoadmapId = null;
    this.currentSvgFile = null;

    this.initEventListeners();
  }

  initEventListeners() {
    if (!this.containerEl || !this.stageEl) return;

    // Mouse Drag (Pan)
    this.containerEl.addEventListener('mousedown', (e) => {
      // Ignora clique em botões ou controles
      if (e.target.closest('.svg-floating-toolbar') || e.target.closest('button')) return;
      this.isDragging = true;
      this.startX = e.clientX - this.translateX;
      this.startY = e.clientY - this.translateY;
      this.containerEl.style.cursor = 'grabbing';
    });

    window.addEventListener('mousemove', (e) => {
      if (!this.isDragging) return;
      this.translateX = e.clientX - this.startX;
      this.translateY = e.clientY - this.startY;
      this.applyTransform();
    });

    window.addEventListener('mouseup', () => {
      if (this.isDragging) {
        this.isDragging = false;
        if (this.containerEl) {
          this.containerEl.style.cursor = 'grab';
        }
      }
    });

    // Roda do Mouse (Zoom centrado no ponteiro)
    this.containerEl.addEventListener('wheel', (e) => {
      e.preventDefault();
      const rect = this.containerEl.getBoundingClientRect();
      const mouseX = e.clientX - rect.left;
      const mouseY = e.clientY - rect.top;

      const delta = e.deltaY < 0 ? 1.15 : 0.85;
      const newScale = Math.min(Math.max(this.scale * delta, this.minScale), this.maxScale);

      // Ajusta translateX e translateY para manter o ponto sob o mouse estático
      this.translateX = mouseX - (mouseX - this.translateX) * (newScale / this.scale);
      this.translateY = mouseY - (mouseY - this.translateY) * (newScale / this.scale);
      this.scale = newScale;

      this.applyTransform();
    }, { passive: false });

    // Touch events para mobile/tablets
    let initialTouchDist = 0;
    this.containerEl.addEventListener('touchstart', (e) => {
      if (e.touches.length === 1) {
        this.isDragging = true;
        this.startX = e.touches[0].clientX - this.translateX;
        this.startY = e.touches[0].clientY - this.translateY;
      } else if (e.touches.length === 2) {
        this.isDragging = false;
        initialTouchDist = Math.hypot(
          e.touches[0].clientX - e.touches[1].clientX,
          e.touches[0].clientY - e.touches[1].clientY
        );
      }
    });

    this.containerEl.addEventListener('touchmove', (e) => {
      if (e.touches.length === 1 && this.isDragging) {
        this.translateX = e.touches[0].clientX - this.startX;
        this.translateY = e.touches[0].clientY - this.startY;
        this.applyTransform();
      } else if (e.touches.length === 2) {
        const dist = Math.hypot(
          e.touches[0].clientX - e.touches[1].clientX,
          e.touches[0].clientY - e.touches[1].clientY
        );
        const factor = dist / (initialTouchDist || dist);
        const newScale = Math.min(Math.max(this.scale * factor, this.minScale), this.maxScale);
        this.scale = newScale;
        initialTouchDist = dist;
        this.applyTransform();
      }
    }, { passive: true });

    this.containerEl.addEventListener('touchend', () => {
      this.isDragging = false;
    });

    // Teclado
    window.addEventListener('keydown', (e) => {
      if (!this.modalEl || !this.modalEl.classList.contains('open')) return;
      if (e.key === 'Escape') this.close();
      if (e.key === '+' || e.key === '=') this.zoomIn();
      if (e.key === '-' || e.key === '_') this.zoomOut();
      if (e.key === '0') this.resetZoom();
    });

    // Botões da Toolbar
    const zoomInBtn = document.getElementById('btnZoomIn');
    const zoomOutBtn = document.getElementById('btnZoomOut');
    const zoomResetBtn = document.getElementById('btnZoomReset');
    const zoomFitBtn = document.getElementById('btnZoomFit');
    const modalCloseBtn = document.getElementById('btnModalClose');

    if (zoomInBtn) zoomInBtn.addEventListener('click', () => this.zoomIn());
    if (zoomOutBtn) zoomOutBtn.addEventListener('click', () => this.zoomOut());
    if (zoomResetBtn) zoomResetBtn.addEventListener('click', () => this.resetZoom());
    if (zoomFitBtn) zoomFitBtn.addEventListener('click', () => this.fitToScreen());
    if (modalCloseBtn) modalCloseBtn.addEventListener('click', () => this.close());

    // Fechar ao clicar no backdrop (fora da janela)
    if (this.modalEl) {
      this.modalEl.addEventListener('click', (e) => {
        if (e.target === this.modalEl) this.close();
      });
    }
  }

  applyTransform() {
    if (!this.stageEl) return;
    this.stageEl.style.transform = `translate(${this.translateX}px, ${this.translateY}px) scale(${this.scale})`;
    if (this.zoomTextEl) {
      this.zoomTextEl.textContent = `${Math.round(this.scale * 100)}%`;
    }
  }

  zoomIn() {
    this.scale = Math.min(this.scale * 1.25, this.maxScale);
    this.applyTransform();
  }

  zoomOut() {
    this.scale = Math.max(this.scale * 0.8, this.minScale);
    this.applyTransform();
  }

  resetZoom() {
    this.scale = 1.0;
    this.translateX = 0;
    this.translateY = 0;
    this.applyTransform();
  }

  fitToScreen() {
    this.scale = 0.85;
    this.translateX = 0;
    this.translateY = 0;
    this.applyTransform();
  }

  open(roadmapId, title, svgFile) {
    this.currentRoadmapId = roadmapId;
    this.currentSvgFile = svgFile || `${roadmapId}.svg`;

    if (this.titleEl) this.titleEl.textContent = title || `Roadmap Clínico ${roadmapId}`;
    if (this.badgeEl) this.badgeEl.textContent = roadmapId;

    this.resetZoom();
    this.loadSvg(this.currentSvgFile);

    if (this.modalEl) {
      this.modalEl.classList.add('open');
      document.body.style.overflow = 'hidden';
    }
  }

  close() {
    if (this.modalEl) {
      this.modalEl.classList.remove('open');
      document.body.style.overflow = '';
    }
  }

  loadSvg(svgFile) {
    if (!this.stageEl) return;
    this.stageEl.innerHTML = `
      <div style="padding: 40px; color: #64748B; font-weight: 600; text-align: center;">
        Carregando vetor ${svgFile}...
      </div>
    `;

    const svgPath = `assets/svgs/${svgFile}`;

    // Tenta carregar via fetch (ideal para servidores web http/https)
    fetch(svgPath)
      .then(response => {
        if (!response.ok) throw new Error('Network response not ok');
        return response.text();
      })
      .then(svgText => {
        this.stageEl.innerHTML = svgText;
        this.resetZoom();
      })
      .catch(() => {
        // Fallback robusto para protocolo local file:// ou restrições de sandbox
        this.stageEl.innerHTML = `
          <img src="${svgPath}" alt="Roadmap ${svgFile}" style="max-width: 95%; max-height: 95%; pointer-events: none;" />
        `;
        this.resetZoom();
      });
  }
}

// Inicializador global
window.SVGViewer = SVGViewer;

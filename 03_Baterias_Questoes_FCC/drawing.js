class DrawingTool {
    constructor() {
        this.initDOM();
        this.initCanvas();
        this.bindEvents();
        this.currentTool = 'cursor'; // 'cursor', 'pen-blue', 'pen-red', 'highlighter', 'eraser'
        this.isDrawing = false;
        this.lastX = 0;
        this.lastY = 0;
    }

    initDOM() {
        // Create canvas
        this.canvas = document.createElement('canvas');
        this.canvas.id = 'drawing-canvas';
        document.body.appendChild(this.canvas);
        this.ctx = this.canvas.getContext('2d');
        
        // Ensure canvas stays in background until activated
        this.canvas.style.position = 'absolute';
        this.canvas.style.top = '0';
        this.canvas.style.left = '0';
        this.canvas.style.pointerEvents = 'none';
        this.canvas.style.zIndex = '999';
    }

    initCanvas() {
        // Match document dimensions
        this.resizeCanvas();
        
        // Resize observer to catch expanding questions
        const resizeObserver = new ResizeObserver(() => {
            this.resizeCanvas(true);
        });
        resizeObserver.observe(document.body);
    }

    resizeCanvas(restore = false) {
        let imageData;
        if (restore && this.canvas.width > 0 && this.canvas.height > 0) {
            try {
                imageData = this.ctx.getImageData(0, 0, this.canvas.width, this.canvas.height);
            } catch(e) {}
        }
        
        const scrollHeight = Math.max(
            document.body.scrollHeight, document.documentElement.scrollHeight,
            document.body.offsetHeight, document.documentElement.offsetHeight,
            document.body.clientHeight, document.documentElement.clientHeight
        );
        
        const scrollWidth = Math.max(
            document.body.scrollWidth, document.documentElement.scrollWidth
        );
        
        this.canvas.width = scrollWidth;
        this.canvas.height = scrollHeight;
        
        if (restore && imageData) {
            this.ctx.putImageData(imageData, 0, 0);
        }
    }

    bindEvents() {
        // Canvas Drawing Events
        this.canvas.addEventListener('mousedown', this.startDrawing.bind(this));
        this.canvas.addEventListener('mousemove', this.draw.bind(this));
        this.canvas.addEventListener('mouseup', this.stopDrawing.bind(this));
        this.canvas.addEventListener('mouseout', this.stopDrawing.bind(this));
        
        // Touch support
        this.canvas.addEventListener('touchstart', (e) => {
            if(e.touches.length === 1) {
                const touch = e.touches[0];
                const mouseEvent = new MouseEvent("mousedown", {
                    clientX: touch.clientX,
                    clientY: touch.clientY
                });
                this.canvas.dispatchEvent(mouseEvent);
            }
        }, {passive: false});
        
        this.canvas.addEventListener('touchmove', (e) => {
            if(e.touches.length === 1) {
                e.preventDefault(); // Prevent scrolling while drawing
                const touch = e.touches[0];
                const mouseEvent = new MouseEvent("mousemove", {
                    clientX: touch.clientX,
                    clientY: touch.clientY
                });
                this.canvas.dispatchEvent(mouseEvent);
            }
        }, {passive: false});
        
        this.canvas.addEventListener('touchend', () => {
            const mouseEvent = new MouseEvent("mouseup", {});
            this.canvas.dispatchEvent(mouseEvent);
        });

        // Toolbar Events (Will be triggered from HTML buttons)
        document.addEventListener('click', (e) => {
            const btn = e.target.closest('.dt-btn');
            if (!btn) return;
            
            const tool = btn.dataset.tool;
            if (tool === 'clear') {
                this.clearCanvas();
                return;
            }
            
            this.setTool(tool);
            
            // Update active state in UI
            document.querySelectorAll('.dt-btn').forEach(b => b.classList.remove('active'));
            if(tool !== 'clear') btn.classList.add('active');
        });
    }
    
    setTool(tool) {
        this.currentTool = tool;
        if (tool === 'cursor') {
            this.canvas.style.pointerEvents = 'none';
        } else {
            this.canvas.style.pointerEvents = 'auto';
        }
    }

    startDrawing(e) {
        if (this.currentTool === 'cursor') return;
        this.isDrawing = true;
        
        const rect = this.canvas.getBoundingClientRect();
        this.lastX = e.clientX - rect.left;
        this.lastY = e.clientY - rect.top;
    }

    draw(e) {
        if (!this.isDrawing) return;
        
        const rect = this.canvas.getBoundingClientRect();
        const currentX = e.clientX - rect.left;
        const currentY = e.clientY - rect.top;
        
        this.ctx.beginPath();
        this.ctx.moveTo(this.lastX, this.lastY);
        this.ctx.lineTo(currentX, currentY);
        
        // Tool Configuration
        this.ctx.lineCap = 'round';
        this.ctx.lineJoin = 'round';
        
        if (this.currentTool === 'pen-blue') {
            this.ctx.globalCompositeOperation = 'source-over';
            this.ctx.strokeStyle = '#2563eb';
            this.ctx.lineWidth = 3;
        } else if (this.currentTool === 'pen-red') {
            this.ctx.globalCompositeOperation = 'source-over';
            this.ctx.strokeStyle = '#ef4444';
            this.ctx.lineWidth = 3;
        } else if (this.currentTool === 'highlighter') {
            this.ctx.globalCompositeOperation = 'multiply';
            this.ctx.strokeStyle = 'rgba(253, 224, 71, 0.4)';
            this.ctx.lineWidth = 20;
        } else if (this.currentTool === 'eraser') {
            this.ctx.globalCompositeOperation = 'destination-out';
            this.ctx.strokeStyle = 'rgba(0,0,0,1)';
            this.ctx.lineWidth = 30;
        }
        
        this.ctx.stroke();
        
        this.lastX = currentX;
        this.lastY = currentY;
    }

    stopDrawing() {
        this.isDrawing = false;
    }

    clearCanvas() {
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
    }
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    window.drawingTool = new DrawingTool();
});

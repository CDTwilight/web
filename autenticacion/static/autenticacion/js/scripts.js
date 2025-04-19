document.addEventListener('DOMContentLoaded', function() {
    // Inicializar gráficas
    initializeCharts();
    
    // Inicializar búsqueda y filtros
    initializeSearch();
    initializeFilters();
    
    // Inicializar funciones de modales
    initializeModals();
});

function initializeCharts() {
    // Gráfica de Actividad por Gestor
    const activityCtx = document.getElementById('activityChart');
    if (activityCtx) {
        new Chart(activityCtx, {
            type: 'bar',
            data: {
                labels: chartData.usernames,
                datasets: [{
                    label: 'Pedidos realizados',
                    data: chartData.pedidos_por_usuario,
                    backgroundColor: 'rgba(54, 162, 235, 0.5)',
                    borderColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true,
                        ticks: { color: 'white' }
                    },
                    x: {
                        ticks: { color: 'white' }
                    }
                },
                plugins: {
                    legend: {
                        labels: { color: 'white' }
                    }
                }
            }
        });
    }

    // Gráfica de Pedidos por Mes
    const ordersCtx = document.getElementById('ordersChart');
    if (ordersCtx) {
        new Chart(ordersCtx, {
            type: 'line',
            data: {
                labels: chartData.meses,
                datasets: [{
                    label: 'Pedidos por mes',
                    data: chartData.pedidos_por_mes,
                    borderColor: 'rgba(75, 192, 192, 1)',
                    tension: 0.1,
                    fill: true,
                    backgroundColor: 'rgba(75, 192, 192, 0.2)'
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true,
                        ticks: { color: 'white' }
                    },
                    x: {
                        ticks: { color: 'white' }
                    }
                },
                plugins: {
                    legend: {
                        labels: { color: 'white' }
                    }
                }
            }
        });
    }
}

function initializeSearch() {
    const searchInput = document.getElementById('searchInput');
    if (searchInput) {
        searchInput.addEventListener('input', function(e) {
            const searchTerm = e.target.value.toLowerCase();
            const rows = document.querySelectorAll('tbody tr');
            let visibleCount = 0;

            rows.forEach(row => {
                const text = row.textContent.toLowerCase();
                const isVisible = text.includes(searchTerm);
                row.style.display = isVisible ? '' : 'none';
                if (isVisible) visibleCount++;
            });

            // Actualizar contador en la card
            document.querySelector('.card.bg-primary h3').textContent = visibleCount;
        });
    }
}

function initializeFilters() {
    document.querySelectorAll('[data-filter]').forEach(button => {
        button.addEventListener('click', function() {
            // Remover clase activa de todos los botones
            document.querySelectorAll('[data-filter]').forEach(btn => 
                btn.classList.remove('active'));
            // Añadir clase activa al botón clickeado
            this.classList.add('active');

            const filter = this.dataset.filter;
            const rows = document.querySelectorAll('tbody tr');
            
            rows.forEach(row => {
                switch(filter) {
                    case 'active':
                        row.style.display = row.querySelector('.badge.bg-success') ? '' : 'none';
                        break;
                    case 'inactive':
                        row.style.display = row.querySelector('.badge.bg-danger') ? '' : 'none';
                        break;
                    case 'recent':
                        // Mostrar usuarios registrados en los últimos 30 días
                        const dateCell = row.querySelector('td:nth-child(6)').textContent;
                        const date = new Date(dateCell.split('/').reverse().join('-'));
                        const daysDiff = (new Date() - date) / (1000 * 60 * 60 * 24);
                        row.style.display = daysDiff <= 30 ? '' : 'none';
                        break;
                    case 'all':
                    default:
                        row.style.display = '';
                }
            });

            // Actualizar contador en la card de Total Gestores
            const visibleRows = Array.from(rows).filter(row => 
                row.style.display !== 'none').length;
            document.querySelector('.card.bg-primary h3').textContent = visibleRows;
        });
    });
}

function initializeModals() {
    // Función para abrir modal de edición
    window.abrirModalEditar = function(userId, username) {
        const form = document.getElementById('formEditarUsuario');
        form.action = `/autenticacion/editar-usuario/${userId}/`;
        document.getElementById('editUserId').value = userId;
        document.getElementById('editUsername').value = username;
        document.getElementById('editPassword').value = '';
        new bootstrap.Modal(document.getElementById('editarUsuarioModal')).show();
    }

    // Función para abrir modal de eliminación
    window.abrirModalEliminar = function(userId) {
        const form = document.getElementById('formEliminarUsuario');
        form.action = `/autenticacion/eliminar-usuario/${userId}/`;
        document.getElementById('deleteUserId').value = userId;
        new bootstrap.Modal(document.getElementById('eliminarUsuarioModal')).show();
    }
}

// Función para mostrar notificaciones toast
function showToast(message, type = 'success') {
    Toastify({
        text: message,
        duration: 3000,
        gravity: "top",
        position: "right",
        backgroundColor: type === 'success' ? "#28a745" : "#dc3545",
        stopOnFocus: true
    }).showToast();
}
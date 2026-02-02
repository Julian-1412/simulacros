

export function eventManagementView() {
    return `
    <div class="admin-container">
        <h2>Gestión de Eventos</h2>
        <form id="event-form" class="event-form">
            <input type="hidden" id="event-id">
            <input type="text" id="event-title" placeholder="Nombre del Evento" required>
            <input type="date" id="event-date" required>
            <input type="number" id="event-capacity" placeholder="Capacidad Máxima" required>
            <textarea id="event-desc" placeholder="Descripción"></textarea>
            <button type="submit" id="btn-save-event">Guardar Evento</button>
        </form>

        <table class="admin-table">
            <thead>
                <tr>
                    <th>Evento</th>
                    <th>Fecha</th>
                    <th>Capacidad</th>
                    <th>Registrados</th>
                    <th>Acciones</th>
                </tr>
            </thead>
            <tbody id="admin-events-list"></tbody>
        </table>
    </div>`;
}
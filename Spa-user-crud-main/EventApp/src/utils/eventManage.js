import { getEvents, createEvent, deleteEvent, updateEvent} from '../services/events.js';
import {getRegist} from '../services/regist.js'

export async function adminEventsLogic() {
    const form = document.getElementById("event-form");
    const tbody = document.getElementById("admin-events-list");
    let editMode = false;
    let currentId = null;

    const render = async () => {
        const events = await getEvents();

        const regs = await getRegist();
        
        tbody.innerHTML = events.map(event => {
            const count = regs.filter(r => r.eventId === event.id).length;
            return `
            <tr>
                <td>${event.title}</td>
                <td>${event.date}</td>
                <td>${event.capacity}</td>
                <td>${count}</td>
                <td>
                    <button class="btn-edit" data-id="${event.id}">Editar</button>
                    <button class="btn-delete" data-id="${event.id}">Eliminar</button>
                </td>
            </tr>`;
        }).join("");

        // Eventos de botones
        document.querySelectorAll(".btn-delete").forEach(btn => {
            btn.onclick = async () => {
                if (confirm("¿Eliminar evento?")) {
                    await deleteEvent(btn.dataset.id);
                    render();
                }
            };
        });

        document.querySelectorAll(".btn-edit").forEach(btn => {
            btn.onclick = () => {
                const event = events.find(e => e.id === btn.dataset.id);
                document.getElementById("event-title").value = event.title;
                document.getElementById("event-date").value = event.date;
                document.getElementById("event-capacity").value = event.capacity;
                document.getElementById("event-desc").value = event.description;
                editMode = true;
                currentId = event.id;
                document.getElementById("btn-save-event").textContent = "Actualizar Evento";
            };
        });
    };

    form.onsubmit = async (e) => {
        e.preventDefault();
        const eventData = {
            title: document.getElementById("event-title").value,
            date: document.getElementById("event-date").value,
            capacity: parseInt(document.getElementById("event-capacity").value),
            description: document.getElementById("event-desc").value
        };

        if (editMode) {
            await updateEvent(currentId, eventData);
            editMode = false;
            currentId = null;
            document.getElementById("btn-save-event").textContent = "Guardar Evento";
        } else {
            await createEvent(eventData);
        }

        form.reset();
        render();
    };

    render();
}
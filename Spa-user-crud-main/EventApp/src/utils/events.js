import { getRegist, createRegist } from '../services/regist.js';
import {getEvents} from '../services/events.js'

export async function userEventsLogic() {
    const grid = document.getElementById("events-grid");
    const userData = JSON.parse(localStorage.getItem("userData"));

    const render = async () => {
        const events = await getEvents();
        
        const regs = await getRegist();

        grid.innerHTML = events.map(event => {
            const eventRegs = regs.filter(r => r.eventId === event.id);
            const isFull = eventRegs.length >= event.capacity;
            const alreadyReg = regs.some(r => r.eventId === event.id && r.userId === userData.userEmail);

            return `
            <div class="event-card">
                <h3>${event.title}</h3>
                <p>${event.description}</p>
                <div class="status-info">
                    <strong>Cupos:</strong> ${eventRegs.length} / ${event.capacity}
                </div>
                ${alreadyReg 
                    ? '<button class="btn-status reg" disabled>Ya estás inscrito</button>' 
                    : isFull 
                        ? '<button class="btn-status full" disabled>Cupos Agotados</button>' 
                        : `<button class="btn-action" data-id="${event.id}" data-title="${event.title}">Inscribirme</button>`
                }
            </div>`;
        }).join("");

        document.querySelectorAll(".btn-action").forEach(btn => {
            btn.onclick = async () => {
                const newReg = {
                    userId: userData.userEmail,
                    eventId: btn.dataset.id,
                    eventTitle: btn.dataset.title,
                    date: new Date().toLocaleDateString()
                };

                await createRegist(newReg);
                alert("¡Te has inscrito exitosamente!");
                render();
            };
        });
    };

    render();
}
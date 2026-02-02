import './styles/style.css';
import {eventsView} from './views/events';
import {loginView} from './views/login';
import {aboutView} from './views/about';
import {registView} from './views/registration';
import {dashboardView} from './views/dashboard';
import { userManagmentView } from './views/usermanagement';
import { checkRouteAccess } from './helpers/auth';
import { updateHeader } from './utils/navUtils';
import { initViewLogic } from './utils/initView';
import { myEventsView } from './views/myEvents';
import { eventManagementView } from './views/eventManagement';


const app = document.getElementById('app');

export const routes = {
  "/events":     { component: eventsView,     private: true },
  "/login":    { component: loginView,    private: false },
  "/about":    { component: aboutView,    private: false },
  "/registration":  { component: registView,  private: false },
  "/usermanagment": {component: userManagmentView, private: true},
  "/dashboard": { component: dashboardView, private: true },
  "/my-events" : {component: myEventsView, private: true},
  "/eventManagement" : {component: eventManagementView, private: true}
};


// 4. Función de Navegación Principal
export function navigate(pathname, addToHistory = true) {
  const allowedRoute = checkRouteAccess(pathname);

  // Actualizar URL
  if (addToHistory) {
    window.history.pushState({}, "", allowedRoute);
  }

  updateHeader();
  // Renderizar HTML
  app.innerHTML = routes[allowedRoute].component();

  // Ejecutar lógica de la vista (Eventos)
  initViewLogic(allowedRoute);
}

window.addEventListener("popstate", () => navigate(window.location.pathname, false));

document.body.addEventListener("click", (e) => {
  if (e.target.matches("[data-link]")) {
    e.preventDefault();
    navigate(e.target.getAttribute("href"));
  }
});

// Inicio de la app
navigate(window.location.pathname);


















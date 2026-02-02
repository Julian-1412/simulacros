import { isAuthenticated } from "../helpers/auth";
import { navigate } from "../main";
import { privateHeaderView } from "../views/privateHeader";
import { publicHeaderView } from "../views/publicHeader";

export function setupBurgerMenu() {
    const navButton = document.querySelector(".menu-btn");
    const navlinks = document.querySelector(".a-container");

  if (!navButton || !navlinks) return; // Evita errores si no existen en esa vista

    navButton.onclick = () => {
        navlinks.classList.toggle("is-active");
    };

    const links = navlinks.querySelectorAll("a");
    links.forEach(link => {
        link.onclick = () => {
            navlinks.classList.remove("is-active");
        };
    });
}

export function updateHeader() {
    const headerContainer = document.getElementById("app-header");
    if (!headerContainer) return;

    const isLoggedIn = isAuthenticated();

  // Inyectamos el componente
    headerContainer.innerHTML = isLoggedIn ? privateHeaderView() : publicHeaderView();

  // Re-activamos el menú hamburguesa cada vez que el header cambia
    setupBurgerMenu();

    if (isLoggedIn) {

    const userBtn = document.getElementById("userMenuBtn");
        const dropdown = document.getElementById("userDropdown");

        // Abrir/Cerrar Dropdown
        userBtn?.addEventListener("click", (e) => {
            e.stopPropagation();
            dropdown.classList.toggle("show-dropdown");
        });

        // Cerrar al hacer clic fuera
        window.onclick = (e) => {
            if (!e.target.matches('.nav-avatar')) {
                dropdown?.classList.remove("show-dropdown");
            }
        };

    document.getElementById("logout")?.addEventListener("click", () => {
        localStorage.removeItem("userData");
        sessionStorage.clear();
        navigate("/login");
    });
    }
}
import '../styles/privateHeader.css'

export function privateHeaderView() {
    const data = JSON.parse(localStorage.getItem("userData"));
    const isAdmin = data.role === "Admin"


    return `
        <nav id="navbar">
            <a>
                <img class="logo-nav" src="./src/assets/time-management.png" alt="logo">
            </a>
            <div class="private-header">
                <div class="a-container">
                ${isAdmin ? `
                    <a data-link class="a-nav" href="/dashboard">Dashboard Eventos</a>
                    <a data-link class="a-nav" href="/eventManagement">Gestion Eventos</a>
                    <a data-link class="a-nav" href="/usermanagment">Usuarios</a>
                ` : `
                    <a data-link class="a-nav" href="/events">Eventos</a>
                    <a data-link class="a-nav" href="/my-events">Mis Eventos</a>
                `}
            </div>
                <div class="user-menu-wrapper">
                    <a id="userMenuBtn" class="user-btn">
                        <img src="./src/assets/user.png" alt="User" class="nav-avatar">
                    </a>
                    <div id="userDropdown" class="dropdown-content">
                            <small>USUARIO</small>
                            <p><strong>${data.userEmail || 'Usuario'}</strong></p>
                            <a class="logout-logo"id="logout"> Cerrar seccion</a>
                    </div>
                </div>
            </div>

            <button class="menu-btn">☰</button>
        </nav>
    `;
}
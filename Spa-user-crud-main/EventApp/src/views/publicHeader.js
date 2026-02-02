
export function publicHeaderView() {

    return `
        <nav id="navbar">
            <a>
                <img class="logo-nav" src="./src/assets/time-management.png" alt="logo">
            </a>
            <div class="a-container">
                <a data-link class="a-nav" href="/about">About</a>
                <a data-link class="a-nav" href="/login">Login</a>
            </div>
                <button class="menu-btn">☰</button>
        </nav>
    `

}
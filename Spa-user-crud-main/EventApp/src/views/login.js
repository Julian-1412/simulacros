import '../styles/login.css'

export function loginView() {
    return `
        <section class="login">
            <p class="login-title">
            <img class="logo-login" src="./src/assets/login.png" alt="logo">
            SGE
            </p>
            <section>
                <h2>Iniciar Sesión</h2>
                <div class="div-login">
                    <input class="input-login" id="userInput" placeholder="Email" />
                    <input class="input-login" id="passInput" type="password" placeholder="Contraseña" />
                    <button id="buttonLogin">Ingresar</button>
                </div>
            </section>
            <p>No tiene una cuenta ? <a data-link href="/registration">Registrarse</a> </p>
        </section>`
}
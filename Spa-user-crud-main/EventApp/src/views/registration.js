import '../styles/registration.css'

export function registView() {
    return `
    <section class="regist-container">
        <h2>REGISTRO DE USUARIOS</h2>
        <p class="login-title">
            <img class="logo-nav" src="./src/assets/add.png" alt="logo">
        </p>
        <section>
            <div class="div-login">
                <input id="nameRegist" placeholder="Nombre Completo" />
                <input id="emailRegist" type="email" placeholder="Email" />
                <input id="passwordRegist" type="password" placeholder="Contraseña" />
                <button id="btnNewRegist">Registrarme</button>
            </div>
        </section>
    </section>                                              
    `
}
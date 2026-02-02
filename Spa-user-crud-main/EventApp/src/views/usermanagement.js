import '../styles/usermanagement.css'

export function userManagmentView() {
    return `
    <section class="managment">
        <h2>Gestion de usuarios</h2>
        <section>
        <h3>Datos de Usuario</h3>
            <div class="data-form">
                <div class="data-input">
                    <input class="user-managment" id="nameInput" placeholder="Nombre del Usuario" />
                    <input class="user-managment" id="emailInput" type="email" placeholder="Email del Usuario" />
                    <input class="user-managment" id="passwordInput" type="password" placeholder="Contraseña del Usuario" />
                    <select class="role-select" name="roles" id="roleInput">
                        <option value="" disabled selected hidden>Role del Usuario</option>
                        <option value="Admin">Admin</option>
                        <option value="User">User</option>
                    </select>
                </div>
                <div class="data-btn">
                    <button id="btnNewUser">Agregar usuario</button>
                    <button id="btnUpdateUser" disabled>Guardar Cambios</button>
                    <button id="btnCancelEdit" class="btn-delete" disabled>Cancelar</button>
                </div>
            </div>
        </section>
        <section id="userCards" class="user-card">
        
        </section>
        <div id="emptyState" class="empty-state">
        <p> No hay usuarios, crea uno </p>
        </div>
    </section>
    `
}
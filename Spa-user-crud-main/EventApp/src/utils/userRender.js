import { createUser, deleteUser, getUsers, updateUser } from "../services/users";

export async function userManagmentLogic() {

    
    const userCards = document.getElementById("userCards");
    const emptyState = document.getElementById("emptyState");
    const nameInput = document.getElementById("nameInput");
    const emailInput = document.getElementById("emailInput");
    const passwordInput = document.getElementById("passwordInput");
    const roleInput = document.getElementById("roleInput");
    const saveButton = document.getElementById("btnNewUser");
    const btnUpdateUser = document.getElementById("btnUpdateUser");
    const btnCancelEdit = document.getElementById("btnCancelEdit");

    let users = [];
    let currentEditingId = null;

    async function loadUser() {
        try {
            users = await getUsers();
            userRender();
        } catch (error) {
            console.error("Error cargando users:", error);
        }
    }
    
    function userRender() {
        userCards.innerHTML = "";
        
        if(users.length === 0) {
            emptyState.style.display = "block";
            return;
        }
        emptyState.style.display = "none";
        
        users.forEach((user) => {
            const div = document.createElement("div");
            
            div.className = "user-item";

            
            div.innerHTML = `
            <div class="user-content">
                <p class="user-info">
                    <span><strong>Name:</strong> ${user.name}</span> 
                    <span><strong>Email:</strong> ${user.email}</span>
                    <span><strong>Password:</strong> ${user.password}</span>
                    <span><strong>Role:</strong> ${user.role}</span>
                </p>
                <div class="user-actions">
                    <button class="btn btn-edit" data-id="${user.id}">Editar</button>
                    <button class="btn btn-delete" data-id="${user.id}">Eliminar</button>
                </div>
            </div>
            
        `;

        const editBtn = div.querySelector(".btn-edit");
        editBtn.addEventListener("click", (e) => editarUser(user.id, e.target));

        const deleteBtn = div.querySelector(".btn-delete");
        deleteBtn.addEventListener("click", () => eliminarUser(user.id));
        
        userCards.appendChild(div);
    });
}

saveButton?.addEventListener("click", async () => {
    const newUser = {
        name: nameInput.value,
        email: emailInput.value,
        password: passwordInput.value,
        role: roleInput.value
    };
    
    if (!newUser.name || !newUser.email || !newUser.password || !newUser.role)
        return alert("completa los campos");
    
    const response = await createUser(newUser);
    
    if (response) {
        console.log("Se guardo el usuario");
        
        nameInput.value = "";
        emailInput.value = "";
        passwordInput.value = "";
        roleInput.value = "";
        
        await loadUser();
    }
});


// 2. Función para preparar la edición (se llama desde el botón de la tarjeta)
async function editarUser(id) {
    const user = users.find((t) => t.id === id);
    if (!user) return;

    // Cargamos los datos en los inputs
    nameInput.value = user.name;
    emailInput.value = user.email;
    passwordInput.value = user.password;
    roleInput.value = user.role;

    // Guardamos el ID que estamos editando
    currentEditingId = id;

    // Cambiamos el estado de los botones (Habilitar Guardar/Cancelar, Deshabilitar Agregar)
    setEditMode(true);
}

// 3. Función para habilitar/deshabilitar botones
function setEditMode(isEditing) {
    saveButton.disabled = isEditing;        // Botón "Agregar"
    btnUpdateUser.disabled = !isEditing;    // Botón "Guardar Cambios"
    btnCancelEdit.disabled = !isEditing;    // Botón "Cancelar"
}

// 4. Listener para el botón "Guardar Cambios" (el que está en el formulario)
btnUpdateUser.onclick = async () => {
    if (!currentEditingId) return;

    const updatedUser = {
        name: nameInput.value,
        email: emailInput.value,
        password: passwordInput.value,
        role: roleInput.value
    };

    try {
        
        // Llamamos a tu servicio fetch con PATCH o PUT
        const response = await updateUser(currentEditingId, updatedUser);
        
        if (response) {
            alert("Usuario actualizado con éxito");
            finalizarProcesoEdicion();
            await loadUser(); // Refrescamos la lista
        }
    } catch (error) {
        console.error("Error al guardar cambios:", error);
        alert("Hubo un error al intentar guardar");
    }
};

// 5. Listener para el botón "Cancelar"
btnCancelEdit.onclick = () => {
    finalizarProcesoEdicion();
};

// 6. Función auxiliar para limpiar y resetear el formulario
function finalizarProcesoEdicion() {
    currentEditingId = null;
    nameInput.value = "";
    emailInput.value = "";
    passwordInput.value = "";
    roleInput.value = "";
    setEditMode(false);
}

async function eliminarUser(id) {
    if(!confirm("¿Estás seguro de que deseas eliminar este usuario?")) {
        return;
    }

    try{
        await deleteUser(id);
        users = users.filter((user) => user.id !==id);
        userRender();
    }catch(error){
        console.error("Error eliminando user:", error);
        alert("Error al eliminar el user");
    }
}

loadUser();
}


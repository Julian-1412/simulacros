import { createUser } from "../services/users";

export async function registUserLogic() {
    
    const nameRegist = document.getElementById("nameRegist");
    const emailRegist = document.getElementById("emailRegist");
    const passwordRegist = document.getElementById("passwordRegist");
    const saveButtonRegist = document.getElementById("btnNewRegist");


    saveButtonRegist?.addEventListener("click", async () => {
        const newUser = {
            name: nameRegist.value,
            email: emailRegist.value,
            password: passwordRegist.value,
            role: "User"
        };
        
        if (!newUser.name || !newUser.email || !newUser.password)
            return alert("completa los campos");
        
        const response = await createUser(newUser);
        
        if (response) {
            alert("Usuario registrado con exito");
            
            nameRegist.value = "";
            emailRegist.value = "";
            passwordRegist.value = "";
            roleInput.value = "";
        }
    });
}

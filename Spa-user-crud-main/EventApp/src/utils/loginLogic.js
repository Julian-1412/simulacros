import { navigate } from "../main";
import { loginUser } from "../services/login";

export async function loginLogic() {
    
    const btn = document.getElementById("buttonLogin");
        btn?.addEventListener("click", async() => {
            const user = document.getElementById("userInput").value;
            const pass = document.getElementById("passInput").value ;
    
            const userResp = await loginUser(user);
    
            if(!userResp){
            alert("User not found");
            return;
            }
            if(userResp.password == pass){
            
            const userObject = {
                userEmail: user,
                userPassword: pass,
                isActive: true,
                role: userResp.role
            }
            localStorage.setItem("userData", JSON.stringify(userObject));
    
            if(userObject.role === "Admin"){
                navigate("/dashboard");
            }else{
                navigate("/events");
            }
            }else{
            alert("Usuario o contraseña incorrecta");
            }
        });
}
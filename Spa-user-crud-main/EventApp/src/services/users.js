export const getUsers = async () => {

    try{
        
        const data = await fetch("http://localhost:3000/usuarios")
        const response = await data.json()
        return response
    }
    catch(error) {
        console.log("Internal error", error);
    }
}

export const createUser = async (user) => {

    try{
        
        const data = await fetch("http://localhost:3000/usuarios", {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(user)
        });
        const response = await data.json()
        return response
    }
    catch(error) {
        console.log("Internal error", error);
    }
}

export const updateUser = async (id, user) => {
    console.log("Enviando PUT a:", `http://localhost:3000/usuarios/${id}`);
    console.log("Datos del body:", JSON.stringify(user));
    try {
        const response = await fetch(`http://localhost:3000/usuarios/${id}`, {
        method: "PUT",
        headers: {
        "Content-Type": "application/json",
        },
        body: JSON.stringify(user),
    });
        const data = await response.json();
        return data;
    } catch (error) {
        console.error("Error updating todo:", error);
        throw error;
    }
};

export const deleteUser = async (id) => {
    try {
        const response = await fetch(`http://localhost:3000/usuarios/${id}`, {
        method: "DELETE",
        });
        return response.ok;
    } catch (error) {
        console.error("Error deleting todo:", error);
        throw error;
    }
};

// fetch(url, opciones)
//   .then(response => response.json())
//   .then(data => console.log(data))
//   .catch(error => console.error('Error:', error));

// export const getUsers = async () => {
//   try {
//     const response = await axios.get(API_URL);
//     return response.data;
//   } catch (error) {
//     console.error('Error fetching users:', error);
//     throw error;
//   }
// };



export const getUserById = async (id) => {
    try{

        const data = await fetch(`http://localhost:3000/usuarios/${id}`)
        const response = await data.json()
    
        return response

    }
    catch(error){
        console.error("Internal error", error);
    }
}
export const getRegist = async () => {
    try{
        const response = await fetch("http://localhost:3000/registros")
        const data = await response.json()
        return data;
    }catch(err) {
        console.log("Error al cargar los registros", err);
    }
}

export const createRegist = async (regist) => {

    try{
        
        const data = await fetch("http://localhost:3000/registros", {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(regist)
        });
        const response = await data.json()
        return response
    }
    catch(error) {
        console.log("Error al crear el registro", error);
    }
}
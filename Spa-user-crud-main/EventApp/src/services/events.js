export const getEvents = async () => {
    try{
        const response = await fetch("http://localhost:3000/eventos")
        const data = await response.json()
        return data;
    }catch(err) {
        console.log("Error al cargar los eventos", err);
    }
}

export const createEvent = async (event) => {

    try{
        
        const data = await fetch("http://localhost:3000/eventos", {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(event)
        });
        const response = await data.json()
        return response
    }
    catch(error) {
        console.log("Error al crear el evento", error);
    }
}

export const updateEvent = async (id, event) => {
    try {
        const response = await fetch(`http://localhost:3000/eventos/${id}`, {
        method: "PUT",
        headers: {
        "Content-Type": "application/json",
        },
        body: JSON.stringify(event),
    });
        const data = await response.json();
        return data;
    } catch (error) {
        console.error("Error editando evento:", error);
    }
};

export const deleteEvent = async (id) => {
    try {
        const response = await fetch(`http://localhost:3000/eventos/${id}`, {
        method: "DELETE",
        });
        return response.ok;
    } catch (error) {
        console.error("Error eliminando evento:", error);
    }
};
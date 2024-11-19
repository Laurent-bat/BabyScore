import { useState } from "react";

const PlayerForm = ({existingPlayer = {}, updateCallback}) => {
    const  [name, setName] = useState(existingPlayer.name || "")


    const updating = Object.entries(existingPlayer).length !==0

    const onSubmit = async (e) => {
        e.preventDefault()

        const data ={
            name
        }
        const url ="http://127.0.0.1:5000/"+ (updating ? `update_player/${existingPlayer.id}` : "create_player")
        const options = {
            method: updating ? "PATCH" : "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        }
        const response = await fetch(url,options)
        if (response.status !== 201 && response.status !== 200) {
            const data = await response.json()
            alert(data.message)
        } else {
            updateCallback()
        }
    }
    return <form onSubmit={onSubmit}>
        <div>
            <label htmlFor="name">Name:</label>
            <input type="text" id="name" value={name} onChange={(e)=> setName(e.target.value)}/>
        </div>
        <button type="submit">{updating ? "Update Player" : "Create Player"}</button>
    </form>
}

export default PlayerForm
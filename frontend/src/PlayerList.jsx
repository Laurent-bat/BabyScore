import React from 'react'

const PlayerList= ({players, updatePlayer, updateCallback}) => {
    const onDelete = async (id) => {
        try {
            const options = {
                method : "DELETE"
            }
            const response = await fetch (`http://127.0.0.1:5000/delete_player/${id}`, options)
            if (response.status ===200) {
                updateCallback()
            } else {
                console.error("Failed to delete player")
            }
        } catch (error) {
            alert(error)
        }
    }

    return <div>
        <h2>Players</h2>
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Attaque ELO</th>
                    <th>ELO + 10</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                {players.map((player) => (
                    <tr key={player.id}>
                        <td>{player.name}</td>
                        <td>{player.attackElo}</td>
                        <td>{player.attackElo}+10</td>
                        <td>
                            <button onClick={() => updatePlayer(player)}>Update</button>
                            <button onClick={() => onDelete(player.id)}>Delete</button>
                        </td>
                    </tr>
                ))}
            </tbody>
        </table>
    </div>
}

export default PlayerList
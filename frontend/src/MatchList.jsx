import React from 'react'

const MatchList= ({matchs, updateMatch, updateCallback}) => {
    const onDelete = async (id) => {
        try {
            const options = {
                method : "DELETE"
            }
            const response = await fetch (`http://127.0.0.1:5000/delete_match/${id}`, options)
            if (response.status ===200) {
                updateCallback()
            } else {
                console.error("Failed to delete match")
            }
        } catch (error) {
            alert(error)
        }
    }

    return <div>
        <h2>Matchs</h2>
        <table>
            <thead>
                <tr>
                    <th>Team blanc</th>
                    <th>Team noire</th>
                    <th>Score</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                {matchs.map((match) => (
                    <tr key={match.id}>
                        <td>{match.white_atk} x {match.white_def}</td>
                        <td>{match.black_atk} x {match.black_def}</td>
                        <td>{match.white_score} - {match.balck_score}</td>
                        <td>
                            <button onClick={() => updateMatch(match)}>Update</button>
                            <button onClick={() => onDelete(match.id)}>Delete</button>
                        </td>
                    </tr>
                ))}
            </tbody>
        </table>
    </div>
}

export default MatchList
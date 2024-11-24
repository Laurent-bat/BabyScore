import { useState } from "react";
import { View,TextInput } from 'react-native';

const MatchForm = ({existingMatch = {}, updateCallback}) => {
    const  [whiteAttack, setWhiteAttack] = useState(existingMatch.white_atk || "")
    const  [whiteDefense, setWhiteDefense] = useState(existingMatch.white_def || "")
    const  [blackAttack, setBlackAttack] = useState(existingMatch.black_atk || "")
    const  [blackDefense, setBlackDefense] = useState(existingMatch.black_def || "")



    const updating = Object.entries(existingMatch).length !==0

    const onSubmit = async (e) => {
        e.preventDefault()

        const data ={
            name
        }
        const url ="http://127.0.0.1:5000/"+ (updating ? `update_match/${existingMatch.id}` : "create_match")
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
    return <View onSubmit={onSubmit}>
            <TextInput style={{height: 40}}
        placeholder={(updating ? `${existingMatch.white_atk}`: "White Attacker")}
        onChangeText={e => setWhiteAttack(e)}
        defaultValue={(updating ? `${existingMatch.white_atk}` : "")}
        />
        <button type="submit">{updating ? "Update Match" : "Create Match"}</button>
    </View>
}

export default MatchForm
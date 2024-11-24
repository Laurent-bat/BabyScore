import { useState, useEffect } from 'react'
import './App.css'
import MatchList from './MatchList'
import MatchForm from './MatchForm'
import PlayerList from './PlayerList'
import PlayerForm from './PlayerForm'



import React from 'react';
import {Text, View} from 'react-native';

const YourApp = () => {
  return (
    <View
      style={{
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
      }}>
      <Text>Try editing me! 🎉</Text>
    </View>
  );
};

export default YourApp;

// function App() {

//   const [matchs, setMatchs]= useState([])
//   const [isModalOpen, setIsModalOpen] = useState(false)
//   const [currentMatch, setCurrentMatch] = useState({})

//   useEffect(() => {
//     fetchMatchs()
//   }, [])

//   const fetchMatchs = async () => {
//     const response = await fetch("http://127.0.0.1:5000/matchs")
//     const data = await response.json()
//     setMatchs(data.matchs)
//     console.log(data.matchs)
//   }

//   const closeModal = () =>  {
//     setIsModalOpen(false)
//     setCurrentMatch({})
//   }

//   const openCreateModal = () => {
//     if (!isModalOpen) setIsModalOpen(true)
//   }

//   const openEditModal = (match) => {
//     if (isModalOpen) return
//     setCurrentMatch(match)
//     setIsModalOpen(true)
//   }

//   const onUpdate = () => {
//     closeModal()
//     fetchMatchs()
//   }

//   return <>
//   <MatchList matchs={matchs} updateMatch={openEditModal} updateCallback={onUpdate}/> 
//   <button onClick={openCreateModal}>Create New match</button>
//   { isModalOpen && <div className='modal'>
//     <div className='modal-content'>
//       <span className='close' onClick={closeModal}>&times;</span>
//       <MatchForm existingMatch={currentMatch} updateCallback={onUpdate}/></div>
//     </div>}
//   </>
// }

// export default App

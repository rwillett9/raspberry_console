import React, { useState, useEffect } from 'react'
import axios from 'axios'


function Wanikani() {
  const [isLoading, setLoading] = useState(true)
  const [username, setUsername] = useState('')

  useEffect(() => {
    axios.get('http://localhost:4433/test')
      .then(res => {
        // update state vars
        setUsername(res.data.username)
        setLoading(false)
      })
      .catch(err => {
        console.error('Error: ', err.message)
      })
  })

  return (
    <div>
      <a href='/'>Back</a>
      <div>WANIKANI SCREEN</div>
      <div>{username}</div>
    </div>
  )
}

export default Wanikani

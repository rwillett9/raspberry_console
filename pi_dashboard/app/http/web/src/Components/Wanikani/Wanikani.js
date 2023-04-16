import React, { useState, useEffect } from 'react'
import axios from 'axios'
import Button from 'react-bootstrap/Button'


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
      <Button href='/'>Back</Button>
      <Button href='/wanikani/reviews'>Recent Reviews</Button>
      <div>WANIKANI SCREEN</div>
      <div>{username}</div>
    </div>
  )
}

export default Wanikani

import React, { useState, useEffect } from 'react'
import axios from 'axios'


function WanikaniReviews() {
  const [isLoading, setLoading] = useState(true)
  const [username, setUsername] = useState('')

  useEffect(() => {
    // axios.get('http://localhost:4433/test')
    //   .then(res => {
    //     // update state vars
    //     setUsername(res.data.username)
    //     setLoading(false)
    //   })
    //   .catch(err => {
    //     console.error('Error: ', err.message)
    //   })
  })

  return (
    <div>
      <a href='/wanikani'>Back</a>
      <div>REVIEWS SCREEN</div>
    </div>
  )
}

export default WanikaniReviews

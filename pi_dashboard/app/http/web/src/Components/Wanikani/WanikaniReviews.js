import React, { useState, useEffect } from 'react'
import axios from 'axios'
import Button from 'react-bootstrap/Button'
import Col from 'react-bootstrap/Col'
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'


function WanikaniReviews() {
  const [isLoading, setLoading] = useState(true)
  const [reviews, setReviews] = useState(true)
  const [kanji, setKanji] = useState(true)
  const stages = ['apprentice', 'guru', 'master', 'enlightened', 'burned']

  useEffect(() => {
    axios.get('http://localhost:4433/recent-reviews')
      .then(res => {
        // update state vars
        setReviews(res.data.reviews)
        setKanji(res.data.subjects)
        setLoading(false)
      })
      .catch(err => {
        console.error('Error: ', err.message)
      })
  }, [])

  return (
    <Container className='m-3'>
      <Row className='justify-content-start my-2'>
        <Col md='auto'>
          <Button href='/wanikani'>Back</Button>
        </Col>
      </Row>
      {isLoading === false &&
        <div>
          <Row className='justify-content-md-center my-2'>
            <Col md='auto'>
              {reviews.percentage}%
            </Col>
          </Row>
          <div className='my-2'>Correct:</div>
          {stages.map(stage => (
            <div key={'correct_' + stage}>
              {Object.keys(reviews.correct).includes(stage) &&
                <Row>
                  {stage.charAt(0).toUpperCase() + stage.slice(1)}:
                  {reviews.correct[stage].map(subject => (
                    <div key={subject.data.subject_id}>
                      {kanji[subject.data.subject_id]['character']}
                    </div>
                  ))}
                </Row>
              }
            </div>
          ))}

          {/* @TODO copy paste for wrong */}

        </div>
      }

    </Container>
  )
}

export default WanikaniReviews

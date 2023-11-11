import React, { useState, useEffect } from 'react'
import axios from 'axios'
import Button from 'react-bootstrap/Button'
import Card from 'react-bootstrap/Card'
import Col from 'react-bootstrap/Col'
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'


function WanikaniReviews() {
  // helper to style each individual item card
  function get_item_style(type) {
    return {
      color: 'white',
      backgroundColor: SUBJECT_TYPES[type],
      fontSize: 28,
      padding: 1
    }
  }

  const [isLoading, setLoading] = useState(true)
  const [reviews, setReviews] = useState(true)
  const [kanji, setKanji] = useState(true)
  const STAGES = ['apprentice', 'guru', 'master', 'enlightened', 'burned']
  // const SUBJECT_TYPES = ['radical', 'kanji', 'vocabulary']
  const SUBJECT_TYPES = {
    'radical': 'dodgerblue',
    'kanji': 'fuchsia',
    'vocabulary': 'darkviolet'
  }

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
          {reviews.stats.total_items === 0 &&
            // no reviews in the last 24 hours display
            <div>NO REVIEWS COMPLETED IN THE LAST 24 HOURS</div>
          }
          {reviews.stats.total_items !== 0 &&
            <div>
              <Row className='justify-content-md-center my-2'>
                <Col md='auto'>
                  {reviews.stats.percentage}%
                </Col>
              </Row>
              <Card className='m-3'>
                <Card style={{backgroundColor: 'lightgreen', fontSize: 32}}>
                  <Row className='justify-content-md-center'>
                    <Col md='auto'>
                      Correct
                    </Col>
                  </Row>
                </Card>
                {STAGES.map(stage => (
                  <div key={'correct_' + stage}>
                    {Object.keys(reviews.correct).includes(stage) &&
                      <div>
                        {stage.charAt(0).toUpperCase() + stage.slice(1)}:
                        {Object.keys(SUBJECT_TYPES).map(type => (
                          <div key={'correct_' + stage + '_' + type}>
                            {Object.keys(reviews.correct[stage]).includes(type) &&
                              <div>
                                {reviews.correct[stage][type].map(subject => (
                                  <Col md='auto' key={subject.data.subject_id}>
                                    <Card style={get_item_style(type)}>
                                      {kanji[subject.data.subject_id]['character']}
                                    </Card>
                                  </Col>
                                ))}
                              </div>
                            }
                          </div>
                        ))}
                      </div>
                    }
                  </div>
                ))}
              </Card>

              {/* @TODO copy paste for wrong */}
            </div>
          }
        </div>
      }

    </Container>
  )
}

export default WanikaniReviews

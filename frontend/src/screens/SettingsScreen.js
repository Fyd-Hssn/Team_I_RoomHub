import React, { useState } from 'react';
import { Container, Row, Col, Button, Form, Card } from 'react-bootstrap';
import { useDispatch } from 'react-redux';
import { updateProfile } from '../actions/userActions'; 
import { useNavigate } from 'react-router-dom'; 

function SettingsScreen() {
  const [bio, setBio] = useState('');
  const [age, setAge] = useState('');
  const [gender, setGender] = useState('');
  const [school, setSchool] = useState('');
  const [pets, setPets] = useState(false);
  const [allergies, setAllergies] = useState('');
  const [budget, setBudget] = useState('');
  const [sleepSchedule, setSleepSchedule] = useState('');

  const dispatch = useDispatch();
  const navigate = useNavigate(); // Instantiate the useNavigate hook

  const submitHandler = (e) => {
    e.preventDefault();
    // Dispatch action to update user profile
    dispatch(updateProfile({ bio, age, gender, school, pets, allergies, budget, sleepSchedule }));
    // Navigate to the listing screen page after the profile update
    navigate('/profile');
  };

  return (
    <Container className="mt-5">
      <Row>
        <Col md={3}></Col>
        <Col md={6}>
          <Card>
            <Card.Header as="h3" className="text-center">
              Complete Your Profile
            </Card.Header>
            <Card.Body>
              <Form onSubmit={submitHandler}>
                <Form.Group className="mb-3">
                  <Form.Label>Bio</Form.Label>
                  <Form.Control
                    as="textarea"
                    rows={3}
                    placeholder="Tell us a bit about yourself"
                    value={bio}
                    onChange={(e) => setBio(e.target.value)}
                  />
                </Form.Group>

                <Form.Group className="mb-3">
                  <Form.Label>Age</Form.Label>
                  <Form.Control
                    type="number"
                    placeholder="Your age"
                    value={age}
                    onChange={(e) => setAge(e.target.value)}
                  />
                </Form.Group>

                <Form.Group className="mb-3">
                  <Form.Label>Gender</Form.Label>
                  <Form.Control
                    as="select"
                    value={gender}
                    onChange={(e) => setGender(e.target.value)}
                  >
                    <option value="">Select...</option>
                    <option value="M">Male</option>
                    <option value="F">Female</option>
                    <option value="O">Other</option>
                  </Form.Control>
                </Form.Group>

                <Form.Group className="mb-3">
                  <Form.Label>School</Form.Label>
                  <Form.Control
                    type="text"
                    placeholder="Your school name"
                    value={school}
                    onChange={(e) => setSchool(e.target.value)}
                  />
                </Form.Group>

                <Form.Group className="mb-3">
                  <Form.Check
                    type="checkbox"
                    label="Do you have pets?"
                    checked={pets}
                    onChange={(e) => setPets(e.target.checked)}
                  />
                </Form.Group>

                <Form.Group className="mb-3">
                  <Form.Label>Allergies</Form.Label>
                  <Form.Control
                    type="text"
                    placeholder="Any allergies?"
                    value={allergies}
                    onChange={(e) => setAllergies(e.target.value)}
                  />
                </Form.Group>

                <Form.Group className="mb-3">
                  <Form.Label>Budget ($)</Form.Label>
                  <Form.Control
                    type="text"
                    placeholder="Your monthly budget"
                    value={budget}
                    onChange={(e) => setBudget(e.target.value)}
                  />
                </Form.Group>

                <Form.Group className="mb-3">
                  <Form.Label>Sleep Schedule</Form.Label>
                  <Form.Control
                    type="text"
                    placeholder="Your typical sleep schedule"
                    value={sleepSchedule}
                    onChange={(e) => setSleepSchedule(e.target.value)}
                  />
                </Form.Group>

                <Button type="submit" variant="primary">Update Profile</Button>
              </Form>
            </Card.Body>
          </Card>
        </Col>
        <Col md={3}></Col>
      </Row>
    </Container>
  );
}

export default SettingsScreen;
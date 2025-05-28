import { useState } from 'react';
import './App.css'

function App() {
  const [selectedOption, setSelectedOption] = useState("");

  const radioChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setSelectedOption(event.target.value);
  };

  const getData = () => {
    let URL = "http://127.0.0.1:5000";

    if (selectedOption == "breeds") {
      URL = URL + "/breeds";
    }

    if (selectedOption == "facts") {
      URL = URL + "/facts";
    }

    if (selectedOption == "groups") {
      URL = URL + "/groups";
    }

    if (selectedOption == "groups_details") {
      URL = URL + "/groups_details";
    }

    fetch(URL)
      .then((res) => res.json())
      .then((data) => console.log("Data:", data))
      .catch((err) => console.error("Error:", err));
  };

  return (
    <>
      <h1>DOG API APP 🐶</h1>
      <h2></h2>
      <div className="card">
        <div className='filter-options'>
          <div className='opt'>
            <input 
              type="radio"
              id="breeds"
              name="filter_option"
              value="breeds"
              onChange={radioChange} />
            <label>Breeds</label>
          </div>
          

          <div className='opt'>
            <input 
              type="radio"
              id="facts"
              name="filter_option"
              value="facts"
              onChange={radioChange} />
            <label>Facts</label>
          </div>
          

          <div className='opt'>
            <input 
              type="radio"
              id="groups"
              name="filter_option"
              value="groups"
              onChange={radioChange} />
            <label>Groups</label>
          </div>

          <div className='opt'>
            <input 
              type="radio" 
              id="groups_details" 
              name="filter_option" 
              value="groups_details"
              onChange={radioChange} />
            <label>Groups Details</label>
          </div>
        </div>

        <div className='button-container'>
          <button onClick={getData}>
            Get Data!
          </button>
        </div>
      </div>
    </>
  )
}

export default App

import './App.css'

function App() {


  return (
    <>
      <h1>DOG API APP 🐶</h1>
      <h2></h2>
      <div className="card">
        <div className='filter-options'>
          <div className='opt'>
            <input type="radio" id="breeds" name="filter_option" value="Breeds" />
            <label>Breeds</label>
          </div>
          

          <div className='opt'>
            <input type="radio" id="facts" name="filter_option" value="Facts" />
            <label>Facts</label>
          </div>
          

          <div className='opt'>
            <input type="radio" id="groups" name="filter_option" value="Groups" />
            <label>Groups</label>
          </div>

          <div className='opt'>
            <input type="radio" id="groups_details" name="filter_option" value="Groups Details" />
            <label>Groups Details</label>
          </div>
        </div>

        <div className='button-container'>
          <button>
            Get Data!
          </button>
        </div>
      </div>
    </>
  )
}

export default App

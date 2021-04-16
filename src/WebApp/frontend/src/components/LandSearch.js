import React, { Component } from "react";
import { render } from "react-dom";

import { ChakraProvider, Button, List, ListItem, Divider } from '@chakra-ui/react'

class LandSearch extends Component {
  constructor(props) {
    super(props);
    this.state = {
      landData : [], //Array to hold returned cities
      loaded: false,
      placeholder: "Loading",
    };

    this.onClickViewAllLand = this.onClickViewAllLand.bind(this);
    this.clearLand = this.clearLand.bind(this);
    this.renderLandList = this.renderLandList.bind(this);
    this.searchLandBySize = this.searchLandBySize.bind(this);
    this.searchLandByNeighboorhood = this.searchLandByNeighboorhood.bind(this);
    this.loadAllLand = this.loadAllLand.bind(this);

    
    
  }

    clearLand(){
        this.setState(state => (
            { landData : [] }
        ))
    }

    onClickViewAllLand()
    {
        this.clearLand();

        fetch("http://127.0.0.1:8000/land")
        .then(response => {
          if (response.status > 400) {
            return this.setState(() => {
              return { placeholder: "Something went wrong!" };
            });
          }
          return response.json();
        })
        .then(landData => {
          this.setState(() => {
            return {
              landData,
            };
          });
        });    
    }

    loadAllLand(_callback)
    {
      this.clearLand();

      fetch("http://127.0.0.1:8000/land")
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(landData => {
        this.setState(() => {
          return {
            landData,
          };
        });
      });    

      _callback();
    }
    renderLandList()
    {
      return (
      <ul>
      {
              this.state.landData.map(landDatum => {
                  return (   <li key={landDatum.address}>
                      address: {landDatum.address} | postalCode: {landDatum.postalCode} | sqrAcres: {landDatum.sqrAcres} | Neighborhood: {landDatum.neighborhoodName}
                  </li>
                  );
              })
      }
    </ul> );
    }

    searchLandBySize()
    {
      var min = prompt("Enter the minimim land size");

      var max = prompt("Enter the maximum land size");

      fetch("http://127.0.0.1:8000/land")
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(landDataRecieved => {
        this.setState(() => {
          return {
            landData : landDataRecieved.filter(function(land){ 
              return (land.sqrAcres >= parseFloat(min) && land.sqrAcres <= parseFloat(max))})
          };
        });
      });    
    }
  
    searchLandByNeighboorhood()
    {
      var neighborhood = prompt("Enter the neighborhood name");


      this.clearLand();

      fetch("http://127.0.0.1:8000/land")
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(landDataRecieved => {
        this.setState(() => {
          return {
            landData : landDataRecieved.filter(function(land){ 
                          return (land.neighborhoodName === neighborhood)})
          };
        });
      });    

  
        

        //Set state
        // this.setState(
        //   {
        //     landData : this.state.landData.filter(function(land){ 
        //               return (land.neighborhoodName === neighborhood)})
        //   }
        // )
  
      
    }

 
  render() {
    return (
        <div>
            <Button onClick={this.onClickViewAllLand}>
                {"View All Land"}
            </Button>    
            <Button onClick={this.searchLandBySize}>
              {"Search land by size (sqrAcres)"}
            </Button>
            <Button onClick={this.searchLandByNeighboorhood}>
              {"Search land by neighboorhood"}
            </Button>
            <Button onClick={this.clearLand}>
                {"Clear Search Results"}
            </Button>
            <hr class="dotted" />  

        {              
            this.renderLandList()
        }
      </div>
    );
  }
}


export default LandSearch;

const container = document.getElementById("landSearch");
render(<LandSearch />, container);



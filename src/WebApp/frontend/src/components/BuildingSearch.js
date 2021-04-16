import React, { Component } from "react";
import { render } from "react-dom";

import { ChakraProvider, Button, List, ListItem, Divider } from '@chakra-ui/react'

class BuildingSearch extends Component {
  constructor(props) {
    super(props);
    this.state = {
      buildingData : [], //Array to hold returned cities
      loaded: false,
      placeholder: "Loading",
    };

    // this.onClickViewAllLand = this.onClickViewAllLand.bind(this);
    // this.clearLand = this.clearLand.bind(this);
    // this.renderLandList = this.renderLandList.bind(this);
    // this.searchLandBySize = this.searchLandBySize.bind(this);
    // this.searchLandByNeighboorhood = this.searchLandByNeighboorhood.bind(this);
    // this.loadAllLand = this.loadAllLand.bind(this);

    this.clearBuilding = this.clearBuilding.bind(this);
    this.onClickViewAllBuilding = this.onClickViewAllBuilding.bind(this);
    this.renderBuildingList = this.renderBuildingList.bind(this);
    this.searchBuildingByStories = this.searchBuildingByStories.bind(this);

    
  }

    clearBuilding(){
        this.setState(state => (
            { buildingData : [] }
        ))
    }

    onClickViewAllBuilding()
    {
        this.clearBuilding();

        fetch("http://127.0.0.1:8000/building")
        .then(response => {
          if (response.status > 400) {
            return this.setState(() => {
              return { placeholder: "Something went wrong!" };
            });
          }
          return response.json();
        })
        .then(buildingData => {
          this.setState(() => {
            return {
              buildingData,
            };
          });
        });    
    }

    searchBuildingByStories()
    {
      var min = prompt("Enter the minimim number of stories");

      var max = prompt("Enter the maximum number of stories");

      fetch("http://127.0.0.1:8000/building")
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(buildingDataRecieved => {
        this.setState(() => {
          return {
            buildingData : buildingDataRecieved.filter(function(building){ 
              return (building.numberOfStories >= parseFloat(min) && building.numberOfStories <= parseFloat(max))})
          };
        });
      });    
    }

    renderBuildingList()
    {
      return (
      <ul>
      {
              this.state.buildingData.map(buildingDatum => {
                  return (   <li key={buildingDatum.land}>
                      address: {buildingDatum.land} | developed by: {buildingDatum.developer} | squareFootage: {buildingDatum.squareFootage} | number of stories: {buildingDatum.numberOfStories} 
                  </li>
                  );
              })
      }
    </ul> );
    }

    // searchLandBySize()
    // {
    //   var min = prompt("Enter the minimim land size");

    //   var max = prompt("Enter the maximum land size");

    //   fetch("http://127.0.0.1:8000/land")
    //   .then(response => {
    //     if (response.status > 400) {
    //       return this.setState(() => {
    //         return { placeholder: "Something went wrong!" };
    //       });
    //     }
    //     return response.json();
    //   })
    //   .then(landDataRecieved => {
    //     this.setState(() => {
    //       return {
    //         landData : landDataRecieved.filter(function(land){ 
    //           return (land.sqrAcres >= parseFloat(min) && land.sqrAcres <= parseFloat(max))})
    //       };
    //     });
    //   });    
    // }
  
    // searchLandByNeighboorhood()
    // {
    //   var neighborhood = prompt("Enter the neighborhood name");


    //   this.clearLand();

    //   fetch("http://127.0.0.1:8000/land")
    //   .then(response => {
    //     if (response.status > 400) {
    //       return this.setState(() => {
    //         return { placeholder: "Something went wrong!" };
    //       });
    //     }
    //     return response.json();
    //   })
    //   .then(landDataRecieved => {
    //     this.setState(() => {
    //       return {
    //         landData : landDataRecieved.filter(function(land){ 
    //                       return (land.neighborhoodName === neighborhood)})
    //       };
    //     });
    //   });    

  
        

        //Set state
        // this.setState(
        //   {
        //     landData : this.state.landData.filter(function(land){ 
        //               return (land.neighborhoodName === neighborhood)})
        //   }
        // )
  
      
    // }

 
  render() {
    return (
        <div>
            <Button onClick={this.onClickViewAllBuilding}>
                {"View All Buildings"}
            </Button>    
            <Button onClick={this.searchBuildingByStories}>
                {"Search Buildings by Number of Stories"}
            </Button>   
            <Button onClick={this.clearBuilding}>
                {"Clear Search Results"}
            </Button>
            <hr class="dotted" />  

        {              
            this.renderBuildingList()
        }
      </div>
    );
  }
}

// <Button onClick={this.searchLandBySize}>
//               {"Search land by size (sqrAcres)"}
//             </Button>
//             <Button onClick={this.searchLandByNeighboorhood}>
//               {"Search land by neighboorhood"}
//             </Button>

export default BuildingSearch;

const container = document.getElementById("buildingSearch");
render(<BuildingSearch />, container);



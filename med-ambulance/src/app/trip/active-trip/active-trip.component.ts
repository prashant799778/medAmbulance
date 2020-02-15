import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-active-trip',
  templateUrl: './active-trip.component.html',
  styleUrls: ['./active-trip.component.css']
})
export class ActiveTripComponent implements OnInit {
  tableHeading = [
    "No", "Trip Id", "Driver Name", "Passenger Name","Trip From", "Trip To","Start Time","View Route"
  ]
  heading='Active Trip'
  constructor() { }

  ngOnInit() {
  }

}

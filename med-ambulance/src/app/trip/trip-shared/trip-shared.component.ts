import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-trip-shared',
  templateUrl: './trip-shared.component.html',
  styleUrls: ['./trip-shared.component.css']
})
export class TripSharedComponent implements OnInit {
  @Input() tableHeading: any;
  @Input() heading: any;
  @Input() data= [];
  constructor() { }

  ngOnInit() {
    
  }

}

import { Component, OnInit } from '@angular/core';
import { UserService } from 'src/app/services/user.service';
import { FormGroup, FormBuilder } from '@angular/forms';

@Component({
  selector: 'app-add-vehicle',
  templateUrl: './add-vehicle.component.html',
  styleUrls: ['./add-vehicle.component.css']
})
export class AddVehicleComponent implements OnInit {
	vehicleForm: FormGroup;
	
	constructor(public userService: UserService,
				public fb: FormBuilder) { 
		this.createTable()
	}

	ngOnInit() {

	}
	createTable(){
		this.vehicleForm = this.fb.group({
			regNumber: [''],
			image: [''],
			registrationDate: [''],
			manufacture: [''],
			fuelType: [''],
			modal: [''],
			type: [''],
			category: ['']
		})
	}
	

}

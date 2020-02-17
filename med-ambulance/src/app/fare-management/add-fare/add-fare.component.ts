import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder } from '@angular/forms';
import { IMyDpOptions } from 'mydatepicker';
import { UserService } from 'src/app/services/user.service';

@Component({
  selector: 'app-add-fare',
  templateUrl: './add-fare.component.html',
  styleUrls: ['./add-fare.component.css']
})
export class AddFareComponent implements OnInit {
  vehicleForm: FormGroup;
	public myDatePickerOptions: IMyDpOptions = {
		dateFormat: 'dd.mm.yyyy',
	};
	
	constructor(public userService: UserService,
				public fb: FormBuilder) { 
		this.createTable()
	}

	ngOnInit() {

	}
	createTable(){
		this.vehicleForm = this.fb.group({
			ambType: [''],
			minFare: [''],
			minDistance: [''],
			waitFare: [''],
			farePerKM: [''],
		})
	}

}

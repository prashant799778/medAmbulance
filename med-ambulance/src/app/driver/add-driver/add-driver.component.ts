import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder } from '@angular/forms';
import { IMyDpOptions } from 'mydatepicker';
import { UserService } from 'src/app/services/user.service';

@Component({
  selector: 'app-add-driver',
  templateUrl: './add-driver.component.html',
  styleUrls: ['./add-driver.component.css']
})
export class AddDriverComponent implements OnInit {
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
			name: [''],
			image: [''],
			address: [''],
			mobileNo: [''],
			email: [''],
			gender: [''],
			// type: [''],
			// category: ['']
		})
	}
}

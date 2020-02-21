import { Component, OnInit } from '@angular/core';
import { UserService } from 'src/app/services/user.service';
import { Router } from '@angular/router';
import { AppSettings } from 'src/app/utils/constant';
import { FormGroup, FormBuilder } from '@angular/forms';
import { IMyDpOptions } from 'mydatepicker';
declare var jQuery: any;

@Component({
  selector: 'app-add-hospital',
  templateUrl: './add-hospital.component.html',
  styleUrls: ['./add-hospital.component.css']
})
export class AddHospitalComponent implements OnInit {
	hospitalForm: FormGroup;
	ambType = []
	public myDatePickerOptions: IMyDpOptions = {
		dateFormat: 'dd.mm.yyyy',
	};
	
	constructor(public userService: UserService,
				public fb: FormBuilder) { 
		this.createTable()
		this.getCategory()
	}

	ngOnInit() {

	}
	createTable(){
		this.hospitalForm = this.fb.group({
			ambType: [''],
			name: [''],
			address: ['']
			
		})
	}

	resetForm(){
		this.hospitalForm.reset();
	}

	submitData(){
		// if(resp['status'] == 'true'){
			console.log("modal")
				jQuery('#mainModal').modal('show')
				this.userService.messageValue('Hospital Inserted successfully')
				setTimeout(() => {
					jQuery('#mainModal').modal('hide')
				}, 2000000000);
		// }
	}
	getCategory(){
		// this.userService.getApiData(AppSettings.selectambulanceMode).then(resp=>{
		// 	this.ambCategory = resp['result'] 
		// })
		this.userService.getApiData(AppSettings.selectambulanceTypeMaster).then(resp=>{
			this.ambType = resp['result']
		})
	}
}	
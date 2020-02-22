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
	facityId = []
	cityData = []
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
			ambulanceId: [''],
			hospitalName: [''],
			address: [''],
			lat: [''],
			lng: [''],
			facilityId: [''],
			cityId: ['']
		})
	}

	resetForm(){
		this.hospitalForm.reset();
	}

	submitData(){
		let data = this.hospitalForm.getRawValue()
		console.log(data)
		this.userService.dataPostApi(data,AppSettings.addhospital).then(resp=>{
			if(resp['status'] == 'true'){
				console.log("modal")
					jQuery('#mainModal').modal('show')
					this.userService.messageValue('Hospital Inserted successfully')
					setTimeout(() => {
						jQuery('#mainModal').modal('hide')
					}, 2000);
					this.hospitalForm.reset();
			}
		})
		
	}
	getCategory(){
		this.userService.getApiData(AppSettings.cityMaster).then(resp=>{
			this.cityData = resp['result'] 
		})
		this.userService.getApiData(AppSettings.facilityMaster).then(resp=>{
			this.facityId = resp['result'] 
		})
		this.userService.getApiData(AppSettings.selectambulanceTypeMaster).then(resp=>{
			this.ambType = resp['result']
		})
	}
}	
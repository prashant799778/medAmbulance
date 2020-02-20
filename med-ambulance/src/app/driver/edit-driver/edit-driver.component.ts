import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder } from '@angular/forms';
import { IMyDpOptions } from 'mydatepicker';
import { UserService } from 'src/app/services/user.service';
import { ActivatedRoute } from '@angular/router';
import { AppSettings } from 'src/app/utils/constant';

@Component({
  selector: 'app-edit-driver',
  templateUrl: './edit-driver.component.html',
  styleUrls: ['./edit-driver.component.css']
})
export class EditDriverComponent implements OnInit {
	driverForm: FormGroup;
	driverId: any;
	ambType = [];
	ambCategory = [];
	public myDatePickerOptions: IMyDpOptions = {
		dateFormat: 'dd.mm.yyyy',
	};
	
	constructor(public userService: UserService,
				public route:ActivatedRoute,
				public fb: FormBuilder) { 
		this.createTable()
		this.getCategory()
	}

	ngOnInit() {
		this.route.queryParams.subscribe(params => {
			this.driverId = params['driverId'];
			let data = {
				'driverId': this.driverId
			}
			this.userService.dataPostApi(data,AppSettings.alldriver).then(resp=>{
				this.setData(resp)
			})
		})	
	}
	createTable(){
		this.driverForm = this.fb.group({
			
			name: [''],
			image: [''],
			address: [''],
			mobileNo: [''],
			email: [''],
			gender: [''],
			joiningDate: [''],

			dlNo: [''],
			pIDNo: [''],
			pIDType: [''],
			status: [''],

			transportModel: [''],
			category: [''],
			ambulanceNo: [''],
			ambulanceModeId: [''],
			ambulanceType: [''],
			fuelType: [''],
			ambulanceFilepath: [''],
			ambulanceFilename: [''],
			
			
			
		})
	}
	setData(resp){
		this.driverForm.get('name').setValue(resp['result'][0].name)
		this.driverForm.get('address').setValue(resp['result'][0].address)
		this.driverForm.get('mobileNo').setValue(resp['result'][0].mobileNo)
		this.driverForm.get('email').setValue(resp['result'][0].email)

		this.driverForm.get('dlNo').setValue(resp['result'][0].dlNo)
		this.driverForm.get('pIDNo').setValue(resp['result'][0].pIDNo)
		this.driverForm.get('pIDType').setValue(resp['result'][0].pIDType)
		this.driverForm.get('status').setValue(resp['result'][0].status)
		this.driverForm.get('transportModel').setValue(resp['result'][0].transportModel)
		this.driverForm.get('ambulanceModeId').setValue(resp['result'][0].ambulanceModeId)
		// this.driverForm.get('ambulanceModeId').setValue(resp['result'][0].ambulanceModeId)
		this.driverForm.get('ambulanceNo').setValue(resp['result'][0].ambulanceNo)
		this.driverForm.get('ambulanceType').setValue(resp['result'][0].ambulanceType)
		this.driverForm.get('fuelType').setValue(resp['result'][0].fuelType)
		this.driverForm.get('ambulanceFilepath').setValue(resp['result'][0].ambulanceFilepath)
		this.driverForm.get('ambulanceFilename').setValue(resp['result'][0].ambulanceFilename)
		
		

		
		
		
		
		



		
		
		
		
		
		
	}
	getCategory(){
		this.userService.getApiData(AppSettings.selectambulanceMode).then(resp=>{
			this.ambCategory = resp['result'] 
		})
		this.userService.getApiData(AppSettings.selectambulanceTypeMaster).then(resp=>{
			this.ambType = resp['result']
		})
	}
}	
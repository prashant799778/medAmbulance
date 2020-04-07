import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { IMyDpOptions } from 'mydatepicker';
import { UserService } from 'src/app/services/user.service';
import { AppSettings } from 'src/app/utils/constant';
import { Router, ActivatedRoute } from '@angular/router';
declare var jQuery: any;

@Component({
  selector: 'app-edit-hospital',
  templateUrl: './edit-hospital.component.html',
  styleUrls: ['./edit-hospital.component.css']
})
export class EditHospitalComponent implements OnInit {
  hospitalForm: FormGroup;
	ambType = []
	facityId = []
	city = []
	hospitalId: any;
	viewEdit: any;
	views: boolean;
	emergencyDepart: boolean;
	empanelType=[]
	labType=[]
	accredType=[]
	serviceType=[]
	hospMasType=[]

	public myDatePickerOptions: IMyDpOptions = {
		dateFormat: 'dd.mm.yyyy',
	};
	
	constructor(public userService: UserService,
				public router: Router,
				public route: ActivatedRoute,
				public fb: FormBuilder) { 
		this.createTable()
		this.getCategory()
	}

	ngOnInit() {
    this.route.queryParams.subscribe(params => {
			this.hospitalId = params['id'];
			// let vie = 
			if( params['view'] == 'view'){
				this.views= false;
				this.viewEdit = 'View'
				this.disableForm()

			}else{
				this.views = true;
				this.viewEdit = 'Edit'
				// this.disableForm()
			}
			let data = {
				'id': this.hospitalId
			}
			this.userService.dataPostApi(data,AppSettings.allHospital).then(resp=>{
				this.setData(resp)
			})
		})	
	}
	createTable(){
		this.hospitalForm = this.fb.group({
			ambulanceId: ['',Validators.required],
			hospitalName: ['',Validators.required],
			address: ['',Validators.required],
			lat: ['',Validators.required],
			lng: ['',Validators.required],
			facilityId: ['',Validators.required],
			cityId: ['',Validators.required],
			id: [''],
			empanelment: [''],

			keyPersonName: [''],
			keyPersonTelephone: [''],
			keyPersonMobileNo: [''],
			keyPersonEmail: [''],
			keyPersonFax: [''],

			accreditaionA: [''],
			accreditaionB: [''],
			accreditaionC: [''],

			emergencyKeyName: [''],
			emergencyKeyMobileNo: [''],
			emergencyKeyDesignation: [''],

			emergencyBed: [''],
			ICUBed: [''],
			generalBed: [''],

			inHouseDoctor: [''],
			inHouseSpecialist: [''],

			emergencyDep: [''],
			fixedHours: [''],
			specialities: [''],
			beds: [''],
			eName: [''],
			ename1:['']
		})
		this.hospitalForm.get('eName').valueChanges.subscribe(value=>{
			console.log('hhhhh11111',value)
			if(value == true){
				this.emergencyDepart= true;
				this.hospitalForm.get('ename1').setValue(false) 
			}
		})
		this.hospitalForm.get('ename1').valueChanges.subscribe(value=>{
			if(value == true){
				this.emergencyDepart= false;
				this.hospitalForm.get('eName').setValue(false)
			}
		})
	}
	initializeForm(){
		//  this.fb.group(
		// facilityIds: ['',Validators.required],	
		// )
	}
  
	disableForm(){
		this.hospitalForm.disable()
	}

	
	// resetForm(){
	// 	this.hospitalForm.reset();
	// }

	updateData(){
		
		if(this.hospitalForm.valid){
			this.hospitalForm.get('id').setValue(this.hospitalId)
			let data = this.hospitalForm.getRawValue();
			this.userService.dataPostApi(data,AppSettings.updateHospital).then(resp=>{
				if(resp['status'] == 'true'){
					console.log("modal")
						jQuery('#mainModal').modal('show')
						this.userService.messageValue('Hospital Update successfully')
						setTimeout(() => {
							jQuery('#mainModal').modal('hide')
						}, 2000);
				}
			})
		}else{
			const controls = this.hospitalForm.controls;
			Object.keys(controls).forEach(controlName => {
				controls[controlName].markAsTouched()
			} );
			return false;
		}
		
		
	}
	getCategory(){
		
		this.userService.getApiData(AppSettings.cityMaster).then(resp=>{
			this.city = resp['result'] 
		})
		this.userService.getApiData(AppSettings.facilityMaster).then(resp=>{
			this.facityId = resp['result'] 
		})
		this.userService.getApiData(AppSettings.selectambulanceTypeMaster).then(resp=>{
			this.ambType = resp['result']
		})
		this.userService.getApiData(AppSettings.empanelmentTypeMaster).then(resp=>{
			this.empanelType = resp['result']
		})
		this.userService.getApiData(AppSettings.hospitalLabotaryMaster).then(resp=>{
			this.labType = resp['result']
		})
		this.userService.getApiData(AppSettings.accreditationMaster).then(resp=>{
			this.accredType = resp['result']
		})
		this.userService.getApiData(AppSettings.hospitalServiceMaster).then(resp=>{
			this.serviceType = resp['result']
		})
		this.userService.getApiData(AppSettings.hospitalTypeMaster).then(resp=>{
			this.hospMasType = resp['result']
		})

		
	}
	setData(resp){
		console.log(resp['result'][0].hospitalName)
		this.hospitalForm.get('hospitalName').setValue(resp['result'][0].hospitalName)
		this.hospitalForm.get('facilityId').setValue(resp['result'][0].facilityId)
		this.hospitalForm.get('ambulanceId').setValue(resp['result'][0].ambulanceId)
		this.hospitalForm.get('lat').setValue(resp['result'][0].lat)
		this.hospitalForm.get('lng').setValue(resp['result'][0].lng)
		this.hospitalForm.get('address').setValue(resp['result'][0].address)
		this.hospitalForm.get('cityId').setValue(resp['result'][0].cityId)
		this.hospitalForm.get('id').setValue(resp['result'][0].id)
	}
}	
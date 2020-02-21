import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder } from '@angular/forms';
import { IMyDpOptions } from 'mydatepicker';
import { UserService } from 'src/app/services/user.service';
import { ActivatedRoute } from '@angular/router';
import { AppSettings } from 'src/app/utils/constant';
declare var jQuery : any;

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
	showBanner: any;
	imageShowDLF: any;
	imageShowDLB: any;
	imageShowPIF: any;
	imageShowPIB: any;
	imageShowV: any;
	imageShowU: any;

	showDLF: boolean;
	showDLB: boolean;
	showPIF: boolean;
	showPIB: boolean;
	views: any;
	viewEdit: any;
	activatedds: boolean;
	counter: number;
	public myDatePickerOptions: IMyDpOptions = {
		dateFormat: 'dd.mm.yyyy',
	};
	
	constructor(public userService: UserService,
				public route:ActivatedRoute,
				public fb: FormBuilder) { 
		this.showBanner = 0;	
		this.counter = 0;			
		this.createTable()
		this.getCategory()
	}

	ngOnInit() {
		this.route.queryParams.subscribe(params => {
			this.driverId = params['driverId'];
			// let vie = 
			if( params['view'] == 'view'){
				this.views= false;
				this.viewEdit = 'View'
				this.disableForm()

			}else{
				this.views = true;
				this.viewEdit = 'Edit'
				this.disableForm()
			}
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
			pIDBackFilepath: [''],
			pIDFrontFilepath: [''],
			dlBackFilepath: [''],
			dlFrontFilepath: [''],

			transportModel: [''],
			category: [''],
			ambulanceNo: [''],
			ambulanceModeId: [''],
			ambulanceType: [''],
			fuelType: [''],
			ambulanceFilepath: [''],
			ambulanceFilename: [''],
		})
		// this.driverForm.get('status').valueChanges.subscribe(value=>{
		// 	console.log(value)
		// 	if(value ){
		// 		console.log(value)
		// 		if(this.counter > 0){
		// 			jQuery('#verifiyModal').modal('show')
		// 		}
		// 		this.counter++;	
					
				
		// 	}
			
			
		// })
	}
	setData(resp){
		this.driverForm.get('name').setValue(resp['result'][0].name)
		this.driverForm.get('address').setValue(resp['result'][0].address)
		this.driverForm.get('mobileNo').setValue(resp['result'][0].mobileNo)
		this.driverForm.get('email').setValue(resp['result'][0].email)
		this.driverForm.get('status').setValue(resp['result'][0].status)

		this.driverForm.get('dlNo').setValue(resp['result'][0].dlNo)
		this.driverForm.get('pIDNo').setValue(resp['result'][0].pIDNo)
		this.driverForm.get('pIDType').setValue(resp['result'][0].pIDType)
		this.driverForm.get('pIDBackFilepath').setValue(resp['result'][0].pIDBackFilepath)
		this.driverForm.get('pIDFrontFilepath').setValue(resp['result'][0].pIDFrontFilepath)
		this.driverForm.get('dlBackFilepath').setValue(resp['result'][0].dlBackFilepath)
		this.driverForm.get('dlFrontFilepath').setValue(resp['result'][0].dlFrontFilepath)
		if(resp['result'][0].dlFrontFilepath){
			this.showDLF = true;
		}
		if(resp['result'][0].dlBackFilepath){
			this.showDLB = true;
		}
		if(resp['result'][0].pIDFrontFilepath){
			this.showPIF= true;
		}
		if(resp['result'][0].pIDBackFilepath){
			this.showPIB = true;
		}
		// if(resp['result'][0].dlFrontFilepath){
		// 	this.showDLF = true;
		// }
		
		this.imageShowDLF = resp['result'][0].dlFrontFilepath
		this.imageShowDLB = resp['result'][0].dlBackFilepath
		this.imageShowPIF = resp['result'][0].pIDFrontFilepath
		this.imageShowPIB = resp['result'][0].pIDBackFilepath
		this.imageShowV = resp['result'][0].ambulanceFilepath
		this.showBanner = 1;

	
	// imageShowU: any;
		
		this.driverForm.get('transportModel').setValue(resp['result'][0].transportModel)
		this.driverForm.get('ambulanceModeId').setValue(resp['result'][0].ambulanceModeId)
		// this.driverForm.get('ambulanceModeId').setValue(resp['result'][0].ambulanceModeId)
		this.driverForm.get('ambulanceNo').setValue(resp['result'][0].ambulanceNo)
		this.driverForm.get('ambulanceType').setValue(resp['result'][0].ambulanceType)
		this.driverForm.get('fuelType').setValue(resp['result'][0].fuelType)
		this.driverForm.get('ambulanceFilepath').setValue(resp['result'][0].ambulanceFilepath)
		this.driverForm.get('ambulanceFilename').setValue(resp['result'][0].ambulanceFilename)
	}

	disableForm(){
		this.driverForm.disable();
	}
	
	getCategory(){
		this.userService.getApiData(AppSettings.selectambulanceMode).then(resp=>{
			this.ambCategory = resp['result'] 
		})
		this.userService.getApiData(AppSettings.selectambulanceTypeMaster).then(resp=>{
			this.ambType = resp['result']
		})
	}

	zoomImage(imgPath){
		console.log(imgPath)
		this.userService.imagePath(imgPath)
		jQuery('#zoomImageModal').modal('show')
	}
	// VerifyDriver(){
	// 	let data = {
	// 		'driverId': this.driverId
	// 	}
	// 	this.userService.dataPostApi(data,AppSettings.updateDriverStatus).then(resp=>{
	// 		if(resp['status'] == 'true'){
	// 			let data = {
	// 				'driverId': this.driverId
	// 			}
	// 			this.userService.dataPostApi(data,AppSettings.alldriver).then(resp=>{
	// 				this.setData(resp)
	// 			})
	// 			this.activatedds = true;
	// 			setTimeout(() => {
	// 				jQuery('#verifiyModal').modal('hide')
	// 				setTimeout(()=>{
	// 					this.activatedds = false;
	// 				},1000)
	// 			}, 2000);
	// 		}
	// 	})
	// }
	// VerifiedDriver(){
	// 	jQuery('#verifiyModal').modal('show')
	// }
	// closeModal(){
	// 	jQuery('#verifiyModal').modal('hide')
	// }
}	
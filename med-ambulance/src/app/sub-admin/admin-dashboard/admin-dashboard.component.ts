import { Component, OnInit, OnDestroy } from '@angular/core';
import { UserService } from 'src/app/services/user.service';
import { LocalStorageService } from 'angular-web-storage';
import { AppSettings } from 'src/app/utils/constant';
// import { WebsocketService } from 'src/app/services/websocket.service';
// import { ChatService } from 'src/app/services/chat.service';
import { Subscription } from 'rxjs';
import { MqttService } from 'ngx-mqtt';
import { IMqttMessage } from 'ngx-mqtt';

declare var jQuery: any;

@Component({
  selector: 'app-admin-dashboard',
  templateUrl: './admin-dashboard.component.html',
  styleUrls: ['./admin-dashboard.component.css'],

})
export class AdminDashboardComponent implements OnInit , OnDestroy {
	hospitalID: any;
	currentRideData = []
	pickUp: any;
	dropOff: any;
	status: Array<string> = [];
	userId: any;
	dir = undefined;
	changelat: any = 24.799448;
	changelng: any = 120.979021;
	
	private subscription: Subscription;
	public lat = 28.583980;
public lng = 77.314567;
  public message: string

  public origin: any;
public destination: any;

	constructor(public userService: UserService,
		// private chatService: ChatService,
				private _mqttService: MqttService,
				public local: LocalStorageService) {
					
				
					  this.subscription = this._mqttService.observe('91dbe288564e11ea93d39ebd4d0189fc/ambulanceLiveLocation').subscribe((message: IMqttMessage) => {
						console.log("web sockettttttt",this.userService)
						this.message = message.payload.toString();
					  });
					
				 }

				

				public unsafePublish(topic: string, message: string): void {
					this._mqttService.unsafePublish(topic, message, {qos: 1, retain: true});
				  }
				public ngOnDestroy() {
					this.subscription.unsubscribe();
				  }
	ngOnInit() {
		if(this.local.get('userData1') && this.local.get('userData1').hospitalId){
			this.hospitalID = this.local.get('userData1').hospitalId
			this.getHospitalDashboardData()


		}
		
	}

	getHospitalDashboardData(){
		let data = {
			'hospitalId': this.hospitalID
		}
		this.userService.dataPostApi(data,AppSettings.currentBooking).then(resp=>{
			if(resp['status'] == 'true'){
				this.currentRideData = resp['result']
			}
		})
		
	}
	openMapModal(pickUP, dropOff, userId){
		this.pickUp = pickUP
		this.dropOff = dropOff
		this.userId = userId
		jQuery("#mapModal").modal('show')
		setInterval(()=>{
			this.getDirection()
		},1000)
		
	}


	
  public getDirection() {
    this.dir = {
      origin: { lat: this.changelat, lng: this.changelng },
      destination: { lat: 24.799524, lng: 120.975017 }
	}
	this.changelat = this.changelat - 0.000111;
	this.changelng = this.changelng - 0.000111;
  }

}

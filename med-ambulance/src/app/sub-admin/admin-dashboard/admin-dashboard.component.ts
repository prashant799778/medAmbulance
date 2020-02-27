import { Component, OnInit, OnDestroy } from '@angular/core';
import { UserService } from 'src/app/services/user.service';
import { LocalStorageService } from 'angular-web-storage';
import { AppSettings } from 'src/app/utils/constant';
// import { WebsocketService } from 'src/app/services/websocket.service';
// import { ChatService } from 'src/app/services/chat.service';
import { Subscription } from 'rxjs';
import { MqttService } from 'ngx-mqtt';
import { IMqttMessage } from 'ngx-mqtt';
import { google } from '@agm/core/services/google-maps-types';
// import { google } from 'goo'
// import { MqttService, ConnectionStatus } from 'ngx-mqtt-client';
declare var jQuery: any;

@Component({
  selector: 'app-admin-dashboard',
  templateUrl: './admin-dashboard.component.html',
  styleUrls: ['./admin-dashboard.component.css'],
//   providers: [WebsocketService, ChatService]
})
export class AdminDashboardComponent implements OnInit , OnDestroy {
	hospitalID: any;
	currentRideData = []
	pickUp: any;
	dropOff: any;
	status: Array<string> = [];
	userId: any;
	dir = undefined;
	// directionDisplay = new google.maps.DirectionsRenderer();
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
					var directionDisplay;
//   var directionsService = new google.maps.DirectionsService();
//   var map;

//   function initialize() {
//     // directionsDisplay = new google.maps.DirectionsRenderer();
//     var myOptions = {
//       mapTypeId: google.maps.MapTypeId.ROADMAP,
//     }
//     map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);
//     this.directionsDisplay.setMap(map);

//     var start = '37.7683909618184, -122.51089453697205';
//     var end = '41.850033, -87.6500523';
//     var request = {
//       origin:start, 
//       destination:end,
//       travelMode: google.maps.DirectionsTravelMode.DRIVING
//     };
//     directionsService.route(request, function(response, status) {
//       if (status == google.maps.DirectionsStatus.OK) {
//         this.directionsDisplay.setDirections(response);
//         var myRoute = response.routes[0];
//         var txtDir = '';
//         for (var i=0; i<myRoute.legs[0].steps.length; i++) {
//           txtDir += myRoute.legs[0].steps[i].instructions+"<br />";
//         }
//         document.getElementById('directions').innerHTML = txtDir;
//       }
//     });
//   }




					// this.origin = { lat: 24.799448, lng: 120.979021 };
  					// this.destination = { lat: 24.799524, lng: 120.975017 };
					
					
					  this.subscription = this._mqttService.observe('91dbe288564e11ea93d39ebd4d0189fc/ambulanceLiveLocation').subscribe((message: IMqttMessage) => {
						console.log("web sockettttttt",this.userService)
						this.message = message.payload.toString();
					  });
					// this._mqttService.status().subscribe((s: ConnectionStatus) => {
					// 	const status = s === ConnectionStatus.CONNECTED ? 'CONNECTED' : 'DISCONNECTED';
					// 	this.status.push(`Mqtt client connection status: ${status}`);
					// });
					// chatService.messages.subscribe(msg => {
					// 	console.log("Response from websocket: " + msg);
					//   });
				 }

				//  private message = {
				// 	author: "tutorialedge",
				// 	message: "this is a test message"
				//   };
				
				//   sendMsg() {
				// 	console.log("new message from client to websocket: ", this.message);
				// 	this.chatService.messages.next(this.message);
				// 	this.message.message = "";
				//   }

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


// 			var mqtt = require('mqtt')
// var client  = mqtt.connect('mqtt://test.mosquitto.org')
// console.log("before connect")
// client.on('connect', function () {
// 	console.log("after connect")
//   client.subscribe('presence', function (err) {
//     if (!err) {
//       client.publish('presence', 'Hello mqtt')
//     }
//   })
// })

// client.on('message', function (topic, message) {
//   // message is Buffer
//   console.log(message.toString())
//   client.end()
// })
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
		this.getDirection()
	}


	
  public getDirection() {
    this.dir = {
      origin: { lat: 24.799448, lng: 120.979021 },
      destination: { lat: 24.799524, lng: 120.975017 }
    }
  }

}

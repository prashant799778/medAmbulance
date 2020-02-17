import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule, HttpClient, HTTP_INTERCEPTORS }    from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MyDatePickerModule } from 'mydatepicker';


import { AppComponent } from './app.component';
import { AccountComponent } from './account/account.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { HeaderComponent } from './header/header.component';
import { SideBarComponent } from './side-bar/side-bar.component';

import { ActiveTripComponent } from './trip/active-trip/active-trip.component';
import { CompleteTripComponent } from './trip/complete-trip/complete-trip.component';
import { BookedTripComponent } from './trip/booked-trip/booked-trip.component';
import { RouteMapComponent } from './trip/route-map/route-map.component';
import { TripSharedComponent } from './trip/trip-shared/trip-shared.component';
import { AddDriverComponent } from './driver/add-driver/add-driver.component';
import { AllDriverComponent } from './driver/all-driver/all-driver.component';
import { DriverPaymentComponent } from './driver/driver-payment/driver-payment.component';
import { AllPassengersComponent } from './all-passengers/all-passengers.component';
import { AddVehicleComponent } from './vehicle/add-vehicle/add-vehicle.component';
import { EditVehicleComponent } from './vehicle/edit-vehicle/edit-vehicle.component';
import { ViewAllVehicleComponent } from './vehicle/view-all-vehicle/view-all-vehicle.component';
import { AddFareComponent } from './fare-management/add-fare/add-fare.component';
import { FailListComponent } from './fare-management/fail-list/fail-list.component';

@NgModule({
  declarations: [
    AppComponent,
    AccountComponent,
    DashboardComponent,
    HeaderComponent,
    SideBarComponent,
    ActiveTripComponent,
    CompleteTripComponent,
    BookedTripComponent,
    RouteMapComponent,
    TripSharedComponent,
    AddDriverComponent,
    AllDriverComponent,
    DriverPaymentComponent,
    AllPassengersComponent,
    AddVehicleComponent,
    EditVehicleComponent,
    ViewAllVehicleComponent,
    AddFareComponent,
    FailListComponent,
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    MyDatePickerModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

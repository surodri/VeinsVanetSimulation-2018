//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU Lesser General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
// 
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU Lesser General Public License for more details.
// 
// You should have received a copy of the GNU Lesser General Public License
// along with this program.  If not, see http://www.gnu.org/licenses/.
// 



/*
 * Decider80211pMetrics.cc
 *
 *  Created on: Jan 18, 2018
 *      Author: susanarodriguez
 */

#include "Decider80211pMetrics.h"
#include <../../veins/src/veins/modules/phy/Decider80211p.h>


DeciderResult* Decider80211pMetrics::checkIfSignalOk(AirFrame* frame){
    return Decider80211p::checkIfSignalOk(frame);
}

simtime_t Decider80211pMetrics::processNewSignal(AirFrame* frame){
    return Decider80211p::processNewSignal(frame);
}

simtime_t Decider80211pMetrics::processSignalEnd(AirFrame* frame){
    return Decider80211p::processSignalEnd(frame);
}

void Decider80211pMetrics::switchToTx(){
    Decider80211p::switchToTx();
}

double Decider80211pMetrics::calcChannelSenseRSSI(simtime_t_cref min, simtime_t_cref max){
    return Decider80211p::calcChannelSenseRSSI(min, max);
}

void Decider80211pMetrics::calculateSinrAndSnrMapping(AirFrame* frame, Mapping **sinrMap, Mapping **snrMap){
    Decider80211p::calculateSinrAndSnrMapping(frame, sinrMap, snrMap);
}

void Decider80211pMetrics::finish(){
    Decider80211p::finish();
}
Decider80211pMetrics::~Decider80211pMetrics() {
    Decider80211p::~Decider80211p();
}

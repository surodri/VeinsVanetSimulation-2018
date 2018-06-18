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

#ifndef DECIDER80211PMETRICS_H_
#define DECIDER80211PMETRICS_H_

/*
 * Decider80211pMetrics.h
 *
 *  Created on: Jan 18, 2018
 *      Author: susanarodriguez
 */


#include <../../veins/src/veins/modules/phy/Decider80211p.h>
#include <../../veins/src/veins/base/phyLayer/BaseDecider.h>

class Decider80211pMetrics: public Decider80211p {


    virtual ~Decider80211pMetrics();
protected:

    virtual DeciderResult* checkIfSignalOk(AirFrame* frame);
    virtual simtime_t processNewSignal(AirFrame* frame);
    virtual simtime_t processSignalEnd(AirFrame* frame);
    virtual double calcChannelSenseRSSI(simtime_t_cref min, simtime_t_cref max);
    virtual void calculateSinrAndSnrMapping(AirFrame* frame, Mapping **sinrMap, Mapping **snrMap);
    virtual void finish();
    virtual void switchToTx();
};

#endif /* DECIDER80211PMETRICS_H_ */

#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>
#include "../src/ChannelService.h"

TEST_CASE("RecordQualityReturnsChannelPerTotalChannelsGivenAllZeroCollisions"){

    ChannelService* channelService = new ChannelService();

    REQUIRE(channelService->recordQuality(0, 5)== 1/5);
}

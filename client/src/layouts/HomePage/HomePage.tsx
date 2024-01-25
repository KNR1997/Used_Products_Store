import { Carousel } from "./components/Carousel";
import Dummy from "./components/Dummy";
import { ExploreTopBooks } from "./components/ExploreTopBooks";
import { Heros } from "./components/Heros";
import { LibraryServices } from "./components/LibraryServices";

export const HomePage = () => {
    return (
        <>
            <ExploreTopBooks/>
            {/* <Dummy /> */}
            <Carousel/>
            <Heros/>
            <LibraryServices/>
        </>
    );
}
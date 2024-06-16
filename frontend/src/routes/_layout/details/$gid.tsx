import DetailsPage from "../../../components/Maps/DetailsPage.tsx"
import { createFileRoute } from "@tanstack/react-router"
import 'leaflet/dist/leaflet.css';
export const Route = createFileRoute("/_layout/details/$gid")({
  component: DetailsPage
});
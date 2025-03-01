/**
 * @author: Egide Ntwali
 * @description: The SEO component, It is used to manage the SEO of the website and the pages
 * @param {SeoProps} props The props of the SEO component
 * @param {string} date The date of the SEO component
 * @param {string} templateTitle The template title of the SEO component
 * @returns {JSX.Element} The SEO component
 */

import Head from "next/head";
import { useRouter } from "next/router";

const defaultMeta = {
  title: "Legal AdvisoryAI | AI Powered Legal Advisor",
  siteName: "Legal AdvisoryAI",
  description:
    "Legal AdvisoryAI is an advanced AI-powered legal advisor providing expert legal guidance, document review, and legal insights. Our platform uses cutting-edge artificial intelligence to offer accurate legal support and streamline legal research for individuals and businesses.",
  url: "https://plaxisai.com",
  type: "website",
  robots: "follow, index",
  image:
    "https://res.cloudinary.com/dpqasrwfu/image/upload/v1732817531/bdbc9gzv4homuk8xkk1v.png",
};

type SeoProps = {
  date?: string;
  templateTitle?: string;
} & Partial<typeof defaultMeta>;

export default function Seo(props: SeoProps) {
  const router = useRouter();
  const meta = {
    ...defaultMeta,
    ...props,
  };
  meta["title"] = props.templateTitle
    ? `${props.templateTitle} | ${meta.siteName} - AI Powered Legal Advisor`
    : meta.title;

  return (
    <Head>
      <title>{meta.title}</title>
      <meta
        name="title"
        content="Legal AdvisoryAI | AI Powered Legal Advisor"
      />
      {/* Description */}
      <meta
        name="description"
        content="Legal AdvisoryAI is an advanced AI-powered legal advisor providing expert legal guidance, document review, and legal insights. Our platform uses cutting-edge artificial intelligence to offer accurate legal support and streamline legal research for individuals and businesses."
      />
      {/* Keywords */}
      <meta
        name="keywords"
        content="Legal AdvisoryAI, AI-powered legal advisor, legal guidance, legal document review, legal technology, legal insights, AI legal assistant, legal research, legal support platform, expert legal solutions, AI law, legal tech, legal automation, legal AI tools"
      />
      {/* Author */}
      <meta name="author" content="Egide Ntwari" />
      <meta name="robots" content={meta.robots} />
      <meta content={meta.description} name="description" />
      <meta property="og:url" content={`${meta.url}${router.asPath}`} />
      <link rel="canonical" href={`${meta.url}${router.asPath}`} />
      {/* Open Graph */}
      <meta property="og:type" content={meta.type} />
      <meta property="og:site_name" content={meta.siteName} />
      <meta property="og:description" content={meta.description} />
      <meta property="og:title" content={meta.title} />
      <meta name="image" property="og:image" content={meta.image} />
      {/* Twitter */}
      <meta name="twitter:card" content="summary_large_image" />
      <meta name="twitter:title" content={meta.title} />
      <meta name="twitter:description" content={meta.description} />
      <meta name="twitter:image" content={meta.image} />
      {meta.date && (
        <>
          <meta property="article:published_time" content={meta.date} />
          <meta
            name="publish_date"
            property="og:publish_date"
            content={meta.date}
          />
          <meta
            name="author"
            property="article:author"
            content="Egide Ntwari"
          />
        </>
      )}

      {/* Favicons */}
      {favicons.map((linkProps) => (
        <link key={linkProps.href} {...linkProps} />
      ))}
      <meta name="msapplication-TileColor" content="#ffffff" />
      <meta name="msapplication-config" content="/favicon/browserconfig.xml" />
      <meta name="theme-color" content="#ffffff" />
    </Head>
  );
}

const favicons: Array<React.ComponentPropsWithoutRef<"link">> = [
  {
    rel: "apple-touch-icon",
    sizes: "180x180",
    href: "/favicon/apple-touch-icon.png",
  },
  {
    rel: "icon",
    type: "image/png",
    sizes: "32x32",
    href: "/favicon/favicon-32x32.png",
  },
  {
    rel: "icon",
    type: "image/png",
    sizes: "16x16",
    href: "/favicon/favicon-16x16.png",
  },
  { rel: "manifest", href: "/favicon/site.webmanifest" },
  {
    rel: "mask-icon",
    href: "/favicon/safari-pinned-tab.svg",
    color: "#00e887",
  },
  { rel: "shortcut icon", href: "/favicon/favicon.ico" },
];

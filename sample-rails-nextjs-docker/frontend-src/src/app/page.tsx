import { Container, Typography, Box, Button, Stack } from '@mui/material';
import ExampleApiUsage from '@/components/ExampleApiUsage';

export default function Home() {
  return (
    <Container maxWidth="lg">
      <ExampleApiUsage />
      <Box sx={{ py: 8 }}>
        <Stack spacing={4} alignItems="center">
          <Typography variant="h2" component="h1" align="center">
            Welcome to Our Application
          </Typography>

          <Typography variant="h5" component="h2" align="center" color="text.secondary">
            A modern web application built with Next.js and Ruby on Rails
          </Typography>

          <Box sx={{ mt: 4 }}>
            <Button variant="contained" size="large" href="/about">
              Get Started
            </Button>
          </Box>
        </Stack>
      </Box>
    </Container>
  );
}
